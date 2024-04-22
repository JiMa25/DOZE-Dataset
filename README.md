DOZE: A Dataset for Open-Vocabulary Zero-Shot Object Navigation in Dynamic Environments
==================================

[![arXiv](https://img.shields.io/badge/cs.cv-arXiv%3A2402.19007-42ba94.svg)](https://arxiv.org/abs/2402.19007)

This repository serves as a guide for evaluating ObjectNav agents in DOZE scene datasets, and reproducing experiments provided in the DOZE paper.

<img src="https://github.com/JiMa25/DOZE-Dataset/assets/top226.jpg">

## Table of contents

- [About](#about)
- [Pre-requisites](#pre-requisites)
- [DOZE dataset](#doze-dataset)
- [DOZE episode dataset](#doze-episode-datasets)
- [Experiment setup](#experiment-setup)
- [Experiment commands](#experiment-commands)



## About

> We propose a Dataset for Open-Vocabulary Zero-Shot Object Navigation in Dynamic Environments (DOZE) that comprises ten high-fidelity 3D scenes with over 18k tasks, aiming to mimic complex, dynamic real-world scenarios. Specifically, DOZE scenes feature multiple moving humanoid obstacles, a wide array of open-vocabulary objects, diverse distinct-attribute objects, and valuable textual hints. Besides, different from existing datasets that only provide collision checking between the agent and static obstacles, we enhance DOZE by integrating capabilities for detecting collisions between the agent and moving obstacles.


## Pre-requisites

Our experiments use Python 3.8.16, CUDA 11.3 and Torch 1.11.0 on Ubuntu 20.04. 

[PaddlePaddle API Key](https://www.paddlepaddle.org.cn/documentation/docs/en/api/index_en.html) - You need to apply for an api for text OCR.

## DOZE dataset

You can download the scene dataset on [DOZE](https://openxlab.org.cn/datasets/JiMa25/DOZE)
### Download
#### Download openxlab
```
# Install openxlab
pip install  openxlab 
# Upgrade openxlab
pip install -U openxlab 
# Login
openxlab login #Log in and enter the corresponding AK/SK
```

#### Download DOZE
```
# Dataset download
openxlab dataset get --dataset-repo JiMa25/DOZE
```

## DOZE episode dataset


## Experiment setup


## Experiment commands

