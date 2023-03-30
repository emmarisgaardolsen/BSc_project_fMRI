#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Mon Apr 11 13:33:48 2022

@author: Sirid & Emma 

Insert the line below to run the script
python /projects/MINDLAB2022_MR-semantics-of-depression/scripts/bachelor_scripts/controls_to_scratch_bachelor_script.py
"""
# %% GET READY
user='emma' # change in sirids script
project = 'MINDLAB2022_MR-semantics-of-depression'
Modality='MR'
Task='demonstrativechoice'


import os
import shutil
import pandas as pd

# series_number har vi i en CSV fil
# så skal vi matche alle mapper i /raw/, der starter med series_number fra den liste 

# making a list of subjects to include from the csv-file 'series_include.csv'
df = pd.read_csv('/projects/MINDLAB2022_MR-semantics-of-depression/scripts/bachelor_scripts/subject_info/series_include.csv') 
include = df['series_number'].tolist() # this list in the format [7, 9, 10, etc.]


my_file = open("/projects/MINDLAB2022_MR-semantics-of-depression/scripts/bachelor_scripts/subject_info/exclude.txt","r")
exclude = my_file.read()
exclude_list = exclude.split(",")
my_file.close()
del exclude_list[-1] # deleting the last element cause the last is empty due to concatenation with ,
print(exclude_list)


# %% DEFINES SOME PATHS
user_path = '/users/emma'
project_path = '/projects/MINDLAB2022_MR-semantics-of-depression'
raw_folder = '/projects/MINDLAB2022_MR-semantics-of-depression/raw'
scr_raw_folder = '/projects/MINDLAB2022_MR-semantics-of-depression/scratch/bachelor_scratch/raw_scratch'
bids_folder = '/projects/MINDLAB2022_MR-semantics-of-depression/scratch/bachelor_scratch/BIDS'

  

#%% DELETE ANY RAW FOLDER ON SCRATCH        
if os.path.exists(scr_raw_folder):        # hvis mappe scr_raw_folder:
    shutil.rmtree(scr_raw_folder, ignore_errors=True)  # delete entire directory tree, errors resulting from failed removals will be ignored
    os.makedirs(scr_raw_folder)    # create directory  



# %% MOVE RAW FILES TO SCRATCH
sub_list=os.listdir(raw_folder)

for sub in sub_list:
    #subject level
    sub_raw_dir= os.path.join(raw_folder, sub)
    sub_scr_raw_dir= os.path.join(scr_raw_folder, sub)
    if not str(sub) in exclude:
        print('copying subject: ', sub)
        shutil.copytree(sub_raw_dir,sub_scr_raw_dir,dirs_exist_ok=True)
print('Raw folder copied')
 

# %% REMOVE SOME REDUNDANT FOLDER NAMES    # * why commented out? because not necessary
#cd_cmd = ' '.join(['cd', scr_raw_folder]) # joining 'cd' and 'scr_raw_folder' with a space ' ' in between. this means 
                                           # that the object cd_cmd == cd scr_raw_folder
#os.system(cd_cmd)                         # interacting with the operating system. so when you run the .py script, the line os.system(cd_cmd) will interact with your operating system (and make scr_raw_folder your working directory)



sub_list=os.listdir(scr_raw_folder)  # defines sub_list as a list containing the names of the entries in the directory scr_raw_folder. if we didn't have the "cd_cmd" command and "os.system(cd_cmd)" from above, we should add the full path to the scr_raw_folder

for sub in sub_list: 
    #subject level
    subdir= os.path.join(scr_raw_folder, sub) # joining 2 path components. the os.path.join() concatenates  scr_raw_folder and sub in a path: 
    if str(sub) in exclude:  # * why this again?
        print('removing subject: ', sub)
        shutil.rmtree(subdir, ignore_errors=True)
        
    else:
        
        subdirnew= os.path.join(scr_raw_folder, 'sub-'+sub) # adding sub number to folder name (so it says sub-0009 and not 0009) 
        #rename subdirs to fit with bidsmapper 
        os.rename(subdir,subdirnew) # renaming directory (but subdir still withou 00xx)
        subdir=subdirnew # * why this step? (this time subdir is defined as sub-00xx)
        sesdir_list=os.listdir(subdir) # defines sesdir_list as a list containing the names of the entries in the directory subdir. subdir is scr_raw_folder/sub-00xx
        #initiate numerator
        sesnum=1
        for sesdirs in sesdir_list:
            #Session level
       
            sesdir= os.path.join(subdir, sesdirs)

            #print(sesdir)
            typedir_list=os.listdir(sesdir)
            for typedirs in typedir_list:
                #Type level (MR/SR/MEG)
                typedir= os.path.join(sesdir, typedirs)
                #Only keep folders from expected modality
                if typedirs !=Modality:
                    tempdir= os.path.join(sesdir, typedir)
                    print('removing: ', typedir)
                    shutil.rmtree(tempdir, ignore_errors=True)
                    typedir_list2=os.listdir(sesdir)
                    if len(typedir_list2)==0:
                        print('removing emty ses: ', sesdir)
                        shutil.rmtree(sesdir, ignore_errors=True)
                else:    
                    scandir_list=os.listdir(typedir)
           
                    for scandirs in scandir_list:
                        #Remove the Physiolog folders * maybe we want to keep physiolog 
                        if 'PhysioLog' in scandirs: # remove if we don't want to remove physiolog
                            print('removing: ', scandirs) # remove if we don't want to remove physiolog
                            tempdir= os.path.join(typedir, scandirs) # remove if we don't want to remove physiolog
                            shutil.rmtree(tempdir, ignore_errors=True) # remove if we don't want to remove physiolog 
                        else:
                            #Rename folders to fit conventions
                            scandirs_new=scandirs
                            scandirs_new=scandirs_new.replace('T1_sequence','T1w') # 
                            scandirs_new=scandirs_new.replace('EPI_sequence_words','task-faceword_bold') #  
                            
                            #Scan level (e.g.scout/BOLD)
                            scandir_old= os.path.join(typedir, scandirs)
                            scandir= os.path.join(typedir, scandirs_new)
                            os.rename(scandir_old,scandir)
                            # Move scans up one level
                            shutil.move(scandir,sesdir)
                    os.rmdir(typedir)
            if os.path.exists(sesdir):
                sesdir_old=sesdir
                #rename sessions to number
                sesdir= os.path.join(subdir, 'ses-'+f'{sesnum:03d}')
                #rename subdirs
                os.rename(sesdir_old,sesdir)
                sesnum=sesnum+1
                scandir_list=os.listdir(sesdir)
                for scandirs in scandir_list:
            
                    scandir=os.path.join(sesdir,scandirs)

                    print(scandir)
                    filedir_list=os.listdir(scandir)
                    filedir= os.path.join(scandir, filedir_list[0])
                    files=os.listdir(filedir)
                    #Move all files one directory up
                    for file in files:
                        filepath= os.path.join(filedir, file)
                        shutil.move(filepath,scandir)
                    #Remove old directory
                    os.rmdir(filedir)
                

#%% RUN BIDSMAPPER
#os.system('bidsmapper -a /projects/Undervisning_CognNeuroSci/scratch/raw/ /projects/Undervisning_CognNeuroSci/scratch/BIDS/ -t /users/mikkel/python_scripts/bidsmap_template.yaml')
#os.system('bidscoiner /projects/Undervisning_CognNeuroSci/scratch/raw/ /projects/Undervisning_CognNeuroSci/scratch/BIDS/' )


#%% EDIT DATA_DESCRIPTION FILE
import json
bids_dd_file=os.path.join(bids_folder,'dataset_description.json')

a_file = open(bids_dd_file)
data = json.load(a_file)
a_file.close()
data['Name']=Task
data['Authors']=['Emma Olsen', 'Sirid Wihlborg']
data['TaskName']=Task

a_file = open(bids_dd_file, "w")
json.dump(data, a_file, indent = 4, sort_keys=True)
a_file.close()


# Closing file
#f.close()