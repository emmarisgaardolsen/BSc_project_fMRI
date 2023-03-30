#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  8 16:17:07 2022

@author: sirid & emma
"""
import pandas as pd
from warnings import filterwarnings

# define subject list: 'subjects'
df = pd.read_csv('/projects/MINDLAB2022_MR-semantics-of-depression/scripts/bachelor_scripts/subject_info/series_include.csv') 
series = df['series_number'].tolist() # this list in the format [7, 9, 10, etc.]
subjects = [str(i).zfill(4) for i in series]

# define project name and path to current wd
proj_name = 'MINDLAB2022_MR-semantics-of-depression' 
qsub_path = '/projects/MINDLAB2022_MR-semantics-of-depression/scripts/bachelor_scripts/fMRIprep/run_fmriprep_parallel' # wdir
    
### CLUSTERBATCH
from stormdb.cluster import ClusterBatch

cb = ClusterBatch(proj_name)

for subject in subjects:
    submit_cmd = 'python /projects/MINDLAB2022_MR-semantics-of-depression/scripts/bachelor_scripts/fMRIprep/run_fmriprep_parallel/run_fmriprep_all.py '+ subject # remembter the space between .py and ' !!!!! 
    cb.add_job(cmd=submit_cmd, queue='highmem.q',n_threads = 6, cleanup = False)

cb.submit()

"""
### CLUSTERJOB 
from stormdb.cluster import ClusterJob

for subject in subjects:

    cmd = 'python run_fmriprep_all.py ' + subject # for christ sake please remember ' ' after the .py
    cj = ClusterJob(cmd=cmd,
                    queue='highmem.q',
                    n_threads=6,
                    job_name='py-wrapper_' + subject,
                    proj_name=proj_name,
                    working_dir=qsub_path)
    cj.submit()
"""