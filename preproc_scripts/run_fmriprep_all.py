# this script is an attempt to make fmriprep on each subejct using parallel processing 
# this script should be run my the 'master_sirid.py' script where a function should be defined that loops over this script taking all participants

from sys import argv
import os

def fmriprep_func(subject):
    print('Beginning running fmriprep.')
    os.system('udocker run \
                -v /projects/MINDLAB2022_MR-semantics-of-depression/scratch/bachelor_scratch/BIDS:/in \
                -v /projects/MINDLAB2022_MR-semantics-of-depression/scratch/bachelor_scratch/BIDS/derivatives:/out \
                -v /projects/MINDLAB2022_MR-semantics-of-depression/scripts/bachelor_scripts/fMRIprep/FreeSurfer_license:/fs \
                -v /projects/MINDLAB2022_MR-semantics-of-depression/scratch/bachelor_scratch:/work \
                nipreps/fmriprep:22.0.2 /in /out participant \
                --participant-label sub-{} \
                --ignore sbref \
                --fs-no-reconall --fs-license-file /fs/license.txt -w /work'.format(subject))


subject = argv[1]
    
fmriprep_func(subject)