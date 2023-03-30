import os
import glob



tsv_dir = glob.glob('/projects/MINDLAB2022_MR-semantics-of-depression/scratch/bachelor_scratch/BIDS/*/*scans.tsv')
print(tsv_dir)


for tsv_file in tsv_dir:
    
    with open(tsv_file,'r+') as fp:
        # read all contents from file and store all lines into list
        lines = fp.readlines() 
    
        # move file pointer to the beginning of a file
        fp.seek(0)
    
        # truncate the file
        fp.truncate()

        # start writing lines
        
        # iterate line and line number
        for number, line in enumerate(lines):
            # delete: line number 2,3,5,6,8,9 (remember 0 index)
            if number not in [2,3,5,6,8,9]: # could also be: if 'sbref' in line: 
                fp.write(line)



"""
for tsv_file in tsv_dir:
    
    with open(tsv_file,'r+') as fp:
        # read all contents from file and store all lines into list
        lines = fp.readlines() 
    
        # move file pointer to the beginning of a file
        fp.seek(0)
    
        # truncate the file
        fp.truncate()

        # start writing lines
        
        # iterate line and line number
        for line in enumerate(lines):
            # delete: line number 2,4,7, and 9
            # note: list index starts from 0
            if 'sbref' not in line: # could also be: if 'sbref' in line: 
                fp.write(','.join(line))
"""
