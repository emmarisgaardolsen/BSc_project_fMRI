# importing modules
import os
import pip
from datetime import datetime

now = datetime.now()
print('Time now:',now.strftime("%H:%M:%S"))

######### Install udocker
now = datetime.now()
print('Starting to install udocker:',now.strftime("%H:%M:%S"))

# Using os library instead of command line
os.system('python -m pip install udocker')

now = datetime.now()
print('Finishing udocker install:',now.strftime("%H:%M:%S"))

######### Pull fmriprep
now = datetime.now()
print('Starting to pull:',now.strftime("%H:%M:%S"))

os.system('udocker pull nipreps/fmriprep:latest')
now = datetime.now()
print('Finishing pull:',now.strftime("%H:%M:%S"))

######### Create a container from the pulled image (calling it fprep)
now = datetime.now()
print('Starting to create image:',now.strftime("%H:%M:%S"))

os.system('udocker create --name=fprep22 nipreps/fmriprep:latest')

now = datetime.now()
print('Finishing image creation:',now.strftime("%H:%M:%S"))