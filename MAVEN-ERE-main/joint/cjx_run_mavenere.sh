#!/bin/bash
set -x
module load anaconda/2020.11 cuda/10.2
source activate torch1.10


CUDA_VISIBLE_DEVICES=0 python -u main.py \
    --eval_steps 200 \
    --epochs 100 \
    --lr 3e-4 \
    --bert_lr 2e-5 \
    --accumulation_steps 4 \
    --batch_size 8
