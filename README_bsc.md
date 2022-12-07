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
├── idmdl                      <- csv-files with novelty/transience/resonance
│   └── smoothed               <- csv-files with smoothed signal
├── logs                       
├── newsFluxus                 <- the repo newsFluxus from CHCAA github
├── notebooks                  <- notebooks for plotting      
│   ├── linear_models.ipynb
│   ├── vis_emotionFluxus.ipynb
│   └── ...
├── src                        <- main scripts
│   ├── tweets_bert.py
│   ├── tweets_topic.py
│   ├── summarize_models.py
│   ├── emotionFluxus.py
│   ├── smoothing.py
│   └── ...
├──  summarized_emo            <- ndjson-files with summarized scores of emotion distributions
├──  requirement.txt           <- A requirements file of the required packages.
└──  run.sh                    <- bash script for reproducing results
```

Before running the code you must run the following to install requirements:
```
pip install -r requirements.txt
git clone https://github.com/centre-for-humanities-computing/newsFluxus.git
pip install -r newsFluxus/requirements.txt
```

## 2. Pipeline

### 2.1 Convert your source data to the brain imaging data structure (BIDS) standard
| Do  | File | Output placement |
| --- |:---- |:---------------- |
| Run xxx    |  `src/.../..py    | `…/data/`                 |




We hope this repository is useful and that you find the information you need to complete your analysis. Please feel free to explore the repository and contact us if you have any questions. 

/ Sirid Wihlborg (202007980@post.au.dk)
/ Emma Olsen (2020065072@post.au.dk)


