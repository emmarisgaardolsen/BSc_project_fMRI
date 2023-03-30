#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  8 16:19:35 2022

@author: lau
"""

from sys import argv
import os

"""
def bidscoiner(subject):
    bidsmap = 'bidsmapper -a /projects/MINDLAB2022_MR-semantics-of-depression/scratch/bachelor_scratch/raw_scratch/{} /projects/MINDLAB2022_MR-semantics-of-depression/scratch/bachelor_scratch/BIDS/{} -t /projects/MINDLAB2022_MR-semantics-of-depression/scripts/bachelor_scripts/bidscoin/run_bidscoin/run_bidscoin_emma/bidsmap_template_emma.yaml'.format(subject,subject)
    bidscoin = 'bidscoiner /projects/MINDLAB2022_MR-semantics-of-depression/scratch/bachelor_scratch/raw_scratch/{} /projects/MINDLAB2022_MR-semantics-of-depression/scratch/bachelor_scratch/BIDS/{}'.format(subject,subject)
    os.system(bidsmap)
    os.system(bidscoin)

"""

def bidscoiner(subject):
    bidsmap = 'bidsmapper -a /projects/MINDLAB2022_MR-semantics-of-depression/scratch/bachelor_scratch/raw_scratch /projects/MINDLAB2022_MR-semantics-of-depression/scratch/bachelor_scratch/BIDS -t /projects/MINDLAB2022_MR-semantics-of-depression/scripts/bachelor_scripts/bidscoin/run_bidscoin/run_bidscoin_emma/bidsmap_template_emma.yaml'
    bidscoin = 'bidscoiner /projects/MINDLAB2022_MR-semantics-of-depression/scratch/bachelor_scratch/raw_scratch /projects/MINDLAB2022_MR-semantics-of-depression/scratch/bachelor_scratch/BIDS'
    os.system(bidsmap)
    os.system(bidscoin)
    
subject = argv[1]
    
bidscoiner(subject)


