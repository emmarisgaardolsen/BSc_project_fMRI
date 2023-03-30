import os
import pip

"""
print("I'll start to pull:")
os.system('udocker pull nipreps/fmriprep:latest')
print("Now I'm done pulling fMRIprep and will start creating the image:")
os.system('udocker create --name=fprep22 nipreps/fmriprep:latest')
print("Now, I've created the image :)")
"""

#Performs sanity checks to verify a image available in the local repository.
print(os.popen('udocker verify fprep22').read())

#Prints container metadata. Applies both to container images or to previously extracted containers, accepts both an image or container id as input.
print(os.popen('udocker inspect -p fprep22').read())

#List images available in the local repository, these are images pulled form Docker Hub, and/or load or imported from files.
print(os.popen('udocker images -l').read())

#List extracted containers. These are not processes but containers extracted and available to the executed with udocker run
print(os.popen('udocker ps').read())
print("I'm done")