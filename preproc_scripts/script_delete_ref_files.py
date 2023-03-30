import os
from glob import glob
import shutil

# navigate to a folder containing all ref files (that is, your BIDS folder)
data_folder = os.path.join("/projects/MINDLAB2022_MR-semantics-of-depression/scratch/bachelor_scratch/BIDS")

# listing all the paths to sbref files we want to delete
file_list = glob(os.path.join(data_folder, 'sub-*', 'func', '*sbref*')) # this says, go into all sub-folders and into /func/ folder and find all files that includes the text "sbref"

# deleting the folders
for i in file_list:
    os.remove(i)