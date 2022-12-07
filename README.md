# BSc_project_fMRI - Neuronal Basis of Reading Emotional Words 🧠 💚

![Resonance](fig/header.png)

The current directory contains all of the code and scripts created and used by [Sirid Wihlborg](https://github.com/siridw) & Emma Olsen to analyse functional magnetic resonance imaging (fMRI) data as a part of our bachelor’s thesis at [Cognitive Science](https://bachelor.au.dk/en/cognitivescience), [Aarhus University](https://cc.au.dk/). 

## Table of content 
0. Project description
1. Project Organization
2. Pipeline
3. Description of results obtained from the analysis
4. A detailed description of the methods used to analyse the data.
5. References to any relevant literature consulted during the analysis
6. Acknowledgments

## 0. Project description
The present fMRI study intends to explore and investigate how affective content in the form of visually presented emotional words might be processed differently than neutral words and potentially lead to altered behaviour and enhanced activation in exstrastriate cortex. 

As the brain data contains personal information about individuals, sharing it on a public repository such as GitHub could be in violation of GDPR and put the individuals at risk. As a result, the original brain data is not shared on the current GitHub repository but stored at a server at the Center of Functionally Integrative Neuroscience (CFIN).

## 1.  Project organization
The project is organised as follows:

```
├── README.md                  <- The top-level README for this project.
├── fig                        
├── folder                     <- Some comment
│   └── file                   <- Some comment
├── folder                       
├── folder                     <- Some folder
├── notebooks                  <- Notebooks for XXX     
│   ├── something.ipynb
│   ├── something.ipynb
│   └── ...
├── src                        <- Main scripts
│   ├── something.py
│   ├── something.py
│   ├── something.py
│   ├── something.py
│   ├── something.py
│   └── ...
├──  name                      <- Some files containing smth
├──  requirement.txt           <- A requirements file of the required packages.
└──  file                      <- Something
```

Before running the code you must run the following to install requirements:
```
pip install -r requirements.txt
git clone https://github.com/something.git
```

## 2. Pipelines

### 2.0 Create directory with the correct subjects’ data

| Step | Do                                             | File                         | Output placement |
| ---- | ---------------------------------------------- |:---------------------------- |:---------------- |
| 1     | Create a `.csv` file of the subjects to include. The `.csv` file should contain both sub-id and series number. The current study only investigates the control group containing healthy (i.e., non-depressive) subjects identifiable via their XX ID.                                    |     `series_include.csv`                         |                  |
| 2    | Copy and move the correct subject data from the official `raw` folder to the `scratch` folder from which we can work with it                           | `raw_to_scratch`    | `…/data/` |                  |


### 2.1 Converting source data to the brain imaging data structure (BIDS) standard

The following pipeline assumes that your eventfiles/logfiles are BIDS compatible. Be aware that column names and .json files have to be specified correctly. The pipeline furthermore assumes that you have modifyed your study bidsmap (`bidsmap_template.yaml`) file either via BIDScoin’s GUI or by editing the file directly. 

| Step | Do                                                                                                                | File                                                    | Output placement |
| ---- | ----------------------------------------------------------------------------------------------------------------- |:------------------------------------------------------- |:---------------- |
| 0    | Copy and move logfiles (for the subjects to be analysed only) from `aux` drive to `scratch`                       |   `raw_to_scratch`                                                      |                  |
| 1    | Convert logfiles to BIDS compatible format                                                                        | `convert_logfiles_to_BIDS.py`                           |                  |
| 2    | Delete partphase folders                                                                                          | `delete_partphase_folders.py`                                                        |                  |
| 3    | Dele sbref files                                                                                                  | `script_delete_ref_files.py`                                                        |                  |
| 4    | Delete sbref lines in scantsv file                                                                                | `script_delete_sbref_lines_in_scantsv.py`                                                        |                  |
| 5    | Run the bidsmapper and bidscoiner to make bidscoin conversion                                                     | `bidscoiner_emma.py` | `…/data/`                            |                  |
| 7    | Validate your BIDScoin dataset using the online [BIDS Validator](https://bids-standard.github.io/bids-validator/) | [Link](https://bids-standard.github.io/bids-validator/) |                  |

### 2.2 Preprocessing fMRI data using fMRIPrep

The current pipeline runs fMRIPrep via uDocker. 

| Step | Do                                                                                                                                   | File                       | Output placement    |
| ---- | ------------------------------------------------------------------------------------------------------------------------------------ |:-------------------------- |:------------------- |
| 0    | Create `/BIDS/derivatives` folder to output fMRIPrep                                                                                 |                            |                     |
| 1    | Install uDocker, pull fMRIPrep image and create container from the pulled image                                                      | `full_process_udocker.py`  |                     |
| 2    | Verify fMRIPrep image                                                                                                                | `fmriprep_image_verify.py` |                     |
| 3    | Copy and move the correct subject data from the official `raw` folder to the `scratch` folder from which we can work with it         | `raw_to_scratch`           | `scratch/bachelor_scratch/BIDS`          |
| 4    | Define fMRIPrep function in a script that also calls the function (using `argv`).                                                    | `run_fmriprep_all.py`      |                     |
| 5    | Submit the above script (step 4) to the computer cluster to run fMRIPrep and preprocess the fMRI data of all 34 subjects in parallel | `master.py`                | `/BIDS/derivatives` |

### 2.3 Analysing fMRI data 

| Step | Do                                                   | File                               | Output placement |
| ---- | ---------------------------------------------------- |:---------------------------------- |:---------------- |
| 0    | Prepare eventfiles for analysis                      | `looping_over_all_tsv_files.ipynb` |                  |
| 1    | Define first level model                             | `first_level_fit_function.py`      |                  |
| 2    | Fit first level model on all 34 subjects in parallel | `fit_master.py`                    |  `/flms/`                |
| 3    | Run second level model on all 34 sub                 | `second_level.ipynb`                                   |                  |

### 2.4 Analysing behavioral data 

| Column 1 | Col 2 | Col 3|
|:--|:-:|--:| 
|A|B|C|
|d|e|f| 



We hope this repository is useful and that you find the information you need to complete your analysis. Please feel free to explore the repository and contact us if you have any questions. 

/ Sirid Wihlborg (202007980@post.au.dk)
/ Emma Olsen (2020065072@post.au.dk)


