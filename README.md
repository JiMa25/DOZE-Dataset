DOZE: A Dataset for Open-Vocabulary Zero-Shot Object Navigation in Dynamic Environments
==================================

[![arXiv](https://img.shields.io/badge/cs.cv-arXiv%3A2402.19007-42ba94.svg)](https://arxiv.org/abs/2402.19007)

<img src="https://github.com/JiMa25/DOZE-Dataset/blob/main/assets/DOZE_full.jpeg">


## Table of contents

- [About](#about)
- [Download DOZE dataset](#download-doze-dataset)
- [Quick Start](#quick-start)



## About

<img src="https://github.com/JiMa25/DOZE-Dataset/blob/main/assets/top226.jpg">

> We propose a Dataset for Open-Vocabulary Zero-Shot Object Navigation in Dynamic Environments (DOZE) that comprises ten high-fidelity 3D scenes with over 18k tasks, aiming to mimic complex, dynamic real-world scenarios. Specifically, DOZE scenes feature multiple moving humanoid obstacles, a wide array of open-vocabulary objects, diverse distinct-attribute objects, and valuable textual hints. Besides, different from existing datasets that only provide collision checking between the agent and static obstacles, we enhance DOZE by integrating capabilities for detecting collisions between the agent and moving obstacles.




## Download DOZE dataset

You can download the scene dataset on [DOZE](https://openxlab.org.cn/datasets/JiMa25/DOZE)
### Download openxlab
```
# Install openxlab
pip install  openxlab 
# Upgrade openxlab
pip install -U openxlab 
# Login
openxlab login #Log in and enter the corresponding AK/SK
```

### Download DOZE
```
# Dataset download
openxlab dataset get --dataset-repo JiMa25/DOZE
```

### Decompress DOZE
The `scenes_static.tar.gz` file is a static human obstacle scenes package, the `scenes_dynamic_fixed.tar.gz` file is a fixed trajectory moving human obstacle scenes package, the `scenes_dynamic_random.tar.gz` file is a random trajectory moving human obstacle scenes package. The `episodes.tar.gz` file is the data package for multiple navigation tasks.
```
# Dataset decompress
tar -xzvf scenes_static.tar.gz
tar -xzvf scenes_dynamic_fixed.tar.gz
tar -xzvf scenes_dynamic_random.tar.gz
tar -xzvf episodes.tar.gz
```

### Filesystem Hierarchy
The final hierarchy should look as follows:

```angular2html
~/DOZE
  ├── episodes
  │     ├── Appearance
  |     |     ├── DOZE_0.json
  |     |     ├── DOZE_0.json.gz
  |     |     ├── DOZE_1.json
  |     |     ├── DOZE_1.json.gz
  |     |     ├── ...
  |     |     ├── DOZE_9.json
  |     |     └── DOZE_9.json.gz
  │     ├── Hint
  |     |     ├── DOZE_0.json
  |     |     ├── DOZE_0.json.gz
  |     |     ├── DOZE_1.json
  |     |     ├── DOZE_1.json.gz
  |     |     ├── ...
  |     |     ├── DOZE_9.json
  |     |     └── DOZE_9.json.gz
  │     ├── OV
  |     |     ├── DOZE_0.json
  |     |     ├── DOZE_0.json.gz
  |     |     ├── DOZE_1.json
  |     |     ├── DOZE_1.json.gz
  |     |     ├── ...
  |     |     ├── DOZE_9.json
  |     |     └── DOZE_9.json.gz
  │     └── Spacial
  |           ├── DOZE_0.json
  |           ├── DOZE_0.json.gz
  |           ├── DOZE_1.json
  |           ├── DOZE_1.json.gz
  |           ├── ...
  |           ├── DOZE_9.json
  |           └── DOZE_9.json.gz
  ├── dynamic_fixed
  │     ├── DOZE_dynamic_fixed_0_Data
  │     ├── DOZE_dynamic_fixed_1_Data
  │     ├── ...
  |     ├── DOZE_dynamic_fixed_9_Data
  |     ├── DOZE_dynamic_fixed_0.x86_64
  |     ├── DOZE_dynamic_fixed_1.x86_64
  |     ├── ...
  |     ├── DOZE_dynamic_fixed_9.x86_64
  |     ├── UnityPlayer.so
  |     └── UnityPlayer_s.debug
  ├── dynamic_random
  │     ├── DOZE_dynamic_random_0_Data
  │     ├── DOZE_dynamic_random_1_Data
  │     ├── ...
  |     ├── DOZE_dynamic_random_9_Data
  |     ├── DOZE_dynamic_random_0.x86_64
  |     ├── DOZE_dynamic_random_1.x86_64
  |     ├── ...
  |     ├── DOZE_dynamic_random_9.x86_64
  |     ├── UnityPlayer.so
  |     └── UnityPlayer_s.debug
  └── static
        ├── DOZE_dynamic_random_0_Data
        ├── DOZE_dynamic_random_1_Data
        ├── ... 
        ├── DOZE_dynamic_random_9_Data
        ├── DOZE_dynamic_random_0.x86_64
        ├── DOZE_dynamic_random_1.x86_64
        ├── ...
        ├── DOZE_dynamic_random_9.x86_64
        ├── UnityPlayer.so
        └── UnityPlayer_s.debug
```
The `episodes` folder contains four navigation tasks: Appearance, Spacial, OV (Open-Vocabulary), and Hint. The `static` folder contains 10 3d scenes with static humanoid obstacles, the `dynamic_fixed` folder contains 10 3d scenes with fixed trajectories moving humanoid obstacles, and the `dynamic_random` folder contains 10 3d scenes with random trajectories moving humanoid obstacles. In these scene folders, `DOZE_xxxxxx.x86_64` is the executable file.


## Quick Start

updating...

