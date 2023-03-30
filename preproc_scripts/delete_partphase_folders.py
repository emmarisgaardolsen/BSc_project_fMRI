import os
from glob import glob
import shutil

# for help: https://www.earthdatascience.org/courses/intro-to-earth-data-science/python-code-fundamentals/work-with-files-directories-paths-in-python/os-glob-manipulate-file-paths/

# navigate to folder containing the war data files (organised as: raw_folder/subject/session/scans)
data_folder = os.path.join("/projects/MINDLAB2022_MR-semantics-of-depression/scratch/bachelor_scratch/raw_scratch")

# listing all the folder (part-phase scans) we want to delete
file_list_008 = glob(os.path.join(data_folder, '*', '*', '008*'))
file_list_012 = glob(os.path.join(data_folder, '*', '*', '012*'))
file_list_016 = glob(os.path.join(data_folder, '*', '*', '016*'))

file_list = file_list_008 + file_list_012 + file_list_016

# deleting the folders
for i in file_list:
    shutil.rmtree(i)