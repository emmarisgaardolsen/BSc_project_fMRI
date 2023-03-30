# -*- coding: utf-8 -*-

# import packages

import pandas as pd
import numpy as np
import glob
import csv # for loading the dictionary (include_dict.csv)

# load logfiles 

data_path = '/projects/MINDLAB2022_MR-semantics-of-depression/scratch/bachelor_scratch/logfiles' # define path to logfiles folder (including only relevant logfiles)
search_str = data_path + '/*.csv' # adding '/*.csv' to data_path
file_list = glob.glob(search_str) # list of all logfiles (including paths)

# loop through each file

for i in range(len(file_list)):
    
    file_name = file_list[i] # extracting filename (including path)
    logfile = pd.read_csv(file_name) # load the logfile (converting them into padas dataframe)

    # add 'task' column
    task = np.repeat('demonstrativechoice', len(logfile)) # a list that repeats 'task_name' as many times as the length of the logfile
    logfile['scan_task'] = task # creating task-column to dataframe from list


    # add 'series' column (using include_dict)
    csv_filename = '/projects/MINDLAB2022_MR-semantics-of-depression/scripts/bachelor_scripts/subject_info/include_dict.csv'
    reader = csv.reader(open('/projects/MINDLAB2022_MR-semantics-of-depression/scripts/bachelor_scripts/subject_info/include_dict.csv', 'r'))

    d = {}
    for row in reader:
        k, v = row
        d[k] = v
        keys_values = d.items()
        dict_sub = {str(key):int(value) for key, value in keys_values}
    
    series = np.repeat(dict_sub[str(logfile['ID'][0])], len(logfile)) # using the dictionary to create a list with series number, inserting their sub-ID as dictionary KEY
    logfile['series'] = series # creating 'series'-column to dataframe from list

    # renaming 'onset' column (BIDS conventions)
    logfile.rename(columns={'stim_onset': 'onset'}, inplace=True)
    
    # creating 'duration' column (BIDS conventions)
    logfile['duration'] = 1
    
    # changing positions of columns (onset should be first and duration second) (BIDS conventions)
    logfile=logfile.iloc[:, [9,13,0,1,2,3,4,5,6,7,8,10,11,12]] # you have to print the logfile you just created to get the index position of the different columns 

    # splitting dataframe to three (dependent on run) and saving as .tsv files
    for i in range(1,4): # looping through number 1-3 (because we have run: 1, 2, 3)
        
        logfile_subset = logfile[logfile['block'] == i] # subsetting dataframe for each run
     
        # renaming the file in order with BIDS conventions 
        events_file_name = (
            'sub-'+ str('%04d' % logfile['series'].iloc[0]) + 
            '_task-' + str(logfile_subset['scan_task'].iloc[0]) + 
            '_run-'+ str(logfile_subset['block'].iloc[0]) + 
            '_events.tsv')
        
        # saving the file as .tsv in the BIDS folder
        BIDS_path = (
            '/projects/MINDLAB2022_MR-semantics-of-depression/scratch/bachelor_scratch/BIDS/derivatives/'+ # this path should lead to the BIDS folder with the BIDS converted data
            'sub-' + str('%04d' % logfile['series'].iloc[0]) +
            '/func/')
        events_file_full_name = (BIDS_path + events_file_name) 
        logfile_subset.to_csv(events_file_full_name, na_rep='n/a', index=False, sep="\t", encoding='utf-8') # forcing empty cells to be 'n/a' (BIDS convention), index=False is just to NOT have row names

"""
notes:
- obs* notice the difference in indexing between the original dataframe (logfile) logfile['sub'][0] and the subsettet version (logfile_subset)

- if you want to check the dataframe, BEFORE SUBSETTING then use this chunk 

    events_file_name=('sub-'+ str('%04d' % logfile['sub'][0]) + '_task-' + str(logfile['task'][0]) + '_events.tsv') # test*
    ouput_path='/projects/MINDLAB2022_MR-semantics-of-depression/scratch/bachelor_scratch/event_files_2_subjects/' # test*
    events_full_file_name=(ouput_path+events_file_name) # test*
    logfile.to_csv(events_full_file_name, index=False, sep="\t", encoding='utf-8') # test*
"""
