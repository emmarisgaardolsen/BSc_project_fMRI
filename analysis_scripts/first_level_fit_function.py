# Install packages if necessary
import nilearn
from nilearn.glm.second_level import SecondLevelModel
    
# We need to limit the amount of threads numpy can use, otherwise
# it tends to hog all the CPUs available when using Nilearn
import os
os.environ['MKL_NUM_THREADS'] = '1'
os.environ['OPENBLAS_NUM_THREADS'] = '1'

import pickle


################## DEFINING A FUNCTION THAT FIT FIRST LEVEL MODEL ##################
import os
from sys import argv
import numpy as np
import pandas as pd
import nibabel as nib
from glob import glob
from nilearn import masking
from nilearn.glm.first_level import FirstLevelModel

def fit_firstlevel(sub, bids_dir, run='1', task='demonstrativechoice', space='MNI152NLin2009cAsym', 
                   conf_cols=None, **flm_kwargs):
    """ Example function of how you could implement a complete
    first-level analysis for a single subject. Note that this is
    just one way of implementing this; there may be (much more efficient)
    ways to do this.
    
    Parameters
    ----------
    sub : str
        Subject-identifier (e.g., 'sub-01')
    bids_dir : str
        Path to BIDS directory (root directory)
    task : str
        Name of task to analyse
    run : str
        Name of run to analyze
    space : str
        Name of space of the data
    conf_cols : list (or None)
        List of confound names to include; if None, only 6 motion params
        are included
    **flm_kwargs : kwargs
        Keyword arguments for the FirstLevelModel constructor
    
    Returns
    -------
    flm : FirstLevelModel
        Fitted FirstLevelModel object
    """
    
    # If conf_cols is not set, let's use a "standard" set of
    # motion parameters (translation and rotation in 3 dimensions)
    if conf_cols is None:
        # Note: in new versions of Fmriprep, these variables are named differently,
        # i.e., trans_x, trans_y, trans_z, rot_x, rot_y, rot_z
        conf_cols = ['trans_x', 'trans_y', 'trans_z', 'rot_x', 'rot_y', 'rot_z', 'csf', 'white_matter']

    # We assume it's a BIDS formatted dataset with the Fmriprep outputs in
    # bids_dir/derivatives/fmriprep
    bids_func_dir = os.path.join(bids_dir, sub, 'func')
    fprep_func_dir = os.path.join(bids_dir, 'derivatives', sub, 'func')
    
    # Let's find the fMRI files, given a particular space (e.g., T1w)
    funcs = sorted(glob(os.path.join(fprep_func_dir, f'*space-{space}*-preproc*.nii.gz')))

    # In this loop, we'll find the events/confounds/masks associated with the funcs
    confs, events, masks = [], [], []
    for func in funcs:

        mask_path = func.replace(f'_echo-1_space-{space}_desc-preproc_bold.nii.gz', f'_space-{space}_desc-brain_mask.nii.gz')
        masks.append(mask_path)

        # Find the associated confounds file
        conf_path = func.replace(f'_echo-1_space-{space}_desc-preproc_bold.nii.gz', '_desc-confounds_timeseries.tsv')
        conf_df = pd.read_csv(conf_path, sep='\t').loc[:, conf_cols]
        confs.append(conf_df)
            
        # Find the associated events file
        #event_path = os.path.join(bids_dir, 'derivatives',sub, 'func', f'{sub}_task-{task}_run-{run}_events.tsv') # i replaced this with line below
        event_path = func.replace(f'_echo-1_space-{space}_desc-preproc_bold.nii.gz', '_events.tsv')
        event_df = pd.read_csv(event_path, sep='\t')

        event_df['trial_type'] = 'Neutral'
        event_df.loc[(event_df['Arousal'] > 2) & (event_df['Valence'] < 3), 'trial_type'] = 'Emotional' 
        event_df.loc[(event_df['Arousal'] > 2) & (event_df['Valence'] > 6), 'trial_type'] = 'Emotional' 
        
        events.append(event_df)

        # In case there are multiple masks, create an intersection;
        # if not, this function does nothing
    mask_img = masking.intersect_masks(masks, threshold=0.8)
        
    # Construct the first-level model!
    # We set the t_r to the first func we have, assuming
    # that the TR is the same for each run (if there are multiple runs)
    flm = FirstLevelModel(
        t_r=nib.load(func).header['pixdim'][4],
        slice_time_ref=0.5,
        mask_img=mask_img,
        **flm_kwargs
    )
    
    # Finally, fit the model and return the fitted model
    flm.fit(run_imgs=funcs, events=events, confounds=confs)
    return flm



################## CREATING A LOOP ACROSS 2 SUBJECTS AND ETIMATE A FIRST-LEVEL MODEL FOR EACH ##################
bids_dir = "/projects/MINDLAB2022_MR-semantics-of-depression/scratch/bachelor_scratch/BIDS"

subject = argv[1]

flm = fit_firstlevel(subject, bids_dir, drift_model='cosine', high_pass=0.01) 

file_name = "/projects/MINDLAB2022_MR-semantics-of-depression/scripts/bachelor_scripts/analysis/submit_to_cluster/fitted_flms/flms_final_new/flm_fitted_{}.plk".format(subject)
pickle.dump(flm, open(file_name, 'wb'))