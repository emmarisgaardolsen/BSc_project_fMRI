#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  8 16:17:07 2022

@author: sirid & emma
"""
import pandas as pd
from warnings import filterwarnings

# define subject list: 'subjects'
df = pd.read_csv('../series_include.csv') 
series = df['series_number'].tolist() # this list in the format [7, 9, 10, etc.]
subjects = [str(i).zfill(4) for i in series]
subjects = ["sub-" + i for i in subjects]

# define project name and path to current wd
proj_name = '' 
qsub_path = '../submit_to_cluster' # wdir
    
### CLUSTERBATCH
from stormdb.cluster import ClusterBatch

cb = ClusterBatch(proj_name)

for subject in subjects:
    submit_cmd = 'python path_to_script.py '+ subject # remembter the space between .py and ' !!!!! 
    cb.add_job(cmd=submit_cmd, queue='highmem.q',n_threads = 6, cleanup = False)

cb.submit()