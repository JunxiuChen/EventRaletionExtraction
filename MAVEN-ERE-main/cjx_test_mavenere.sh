#!/bin/bash
set -x
module load anaconda/2020.11 cuda/10.2
source activate torch1.10


CUDA_VISIBLE_DEVICES=0 python -u evaluate.py ./data/MAVEN_ERE/ ./joint/output/42/MAVEN-ERE/
