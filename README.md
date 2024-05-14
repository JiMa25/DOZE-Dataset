DOZE: A Dataset for Open-Vocabulary Zero-Shot Object Navigation in Dynamic Environments
==================================

[![arXiv](https://img.shields.io/badge/cs.cv-arXiv%3A2402.19007-42ba94.svg)](https://arxiv.org/abs/2402.19007)

<img src="https://github.com/JiMa25/DOZE-Dataset/blob/main/assets/DOZE_full.jpeg">


# Table of contents

- [About](#about)
- [Download DOZE dataset](#download-doze-dataset)
- [Quick Start](#quick-start)
- [Citation](#citation)


# About

<img src="https://github.com/JiMa25/DOZE-Dataset/blob/main/assets/top226.jpg">

> We propose a Dataset for Open-Vocabulary Zero-Shot Object Navigation in Dynamic Environments (DOZE) that comprises ten high-fidelity 3D scenes with over 18k tasks, aiming to mimic complex, dynamic real-world scenarios. Specifically, DOZE scenes feature multiple moving humanoid obstacles, a wide array of open-vocabulary objects, diverse distinct-attribute objects, and valuable textual hints. Besides, different from existing datasets that only provide collision checking between the agent and static obstacles, we enhance DOZE by integrating capabilities for detecting collisions between the agent and moving obstacles.




# Download DOZE dataset

You can download the scene dataset on [DOZE](https://openxlab.org.cn/datasets/JiMa25/DOZE)
## Download openxlab
```
# Install openxlab
pip install  openxlab 
# Upgrade openxlab
pip install -U openxlab 
# Login
openxlab login #Log in and enter the corresponding AK/SK
```

## Download DOZE
```
# Dataset download
openxlab dataset get --dataset-repo JiMa25/DOZE
```

## Decompress DOZE
The `scenes_static.tar.gz` file is a static human obstacle scenes package, the `scenes_dynamic_fixed.tar.gz` file is a fixed trajectory moving human obstacle scenes package, the `scenes_dynamic_random.tar.gz` file is a random trajectory moving human obstacle scenes package. The `episodes.tar.gz` file is the data package for multiple navigation tasks.

```
# Dataset decompress
tar -xzvf episodes.tar.gz
mkdir scenes
cd scenes
tar -xzvf ../scenes_static.tar.gz
tar -xzvf ../scenes_dynamic_fixed.tar.gz
tar -xzvf ../scenes_dynamic_random.tar.gz
```

## Filesystem Hierarchy
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
  └──scenes
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

## Episode Structure
Here is an example of the structure of a single episode in our data set.
```json
{
    "id": "Appearance_DOZE_0_274",
    "scene": "DOZE_0",
    "initial_horizon": 10,
    "initial_orientation": 90,
    "initial_position": {
        "x": 0.625999987,
        "y": 0.9,
        "z": 3.20000005
    },
    "goal_object": "a yellow wateringcan",
    "shortest_path": [
        {
            "x": 0.6259999871253967,
            "y": 0.9,
            "z": 3.200000047683716
        },
        {
            "x": -0.14999985694885254,
            "y": 0.9,
            "z": 2.549999952316284
        },
        {
            "x": -1.5299997329711914,
            "y": 0.9,
            "z": -1.499999761581421
        },
        {
            "x": -1.6199997663497925,
            "y": 0.9,
            "z": -1.5899999141693115
        },
        {
            "x": -1.874000072479248,
            "y": 0.9,
            "z": -1.7999999523162842
        }
    ],
    "shortest_path_length": 5.747767802180204
}
```

A `DOZE_x.json` file contains all the tasks in a `DOZE_x` scene. Key parameters include:

- `id`: the index of the task.
- `scene`: the scene for this task.
- `initial_horizon`: the horizon of the agent's initial state. the horizon change's the camera's rotation. Values are clamped between [-30:30].
- `initial_orientation`: The initial rotation of the agent.
- `initial_position`: initial position of the agent.
- `goal_object`: target object.
- `shortest_path`: a dictionary containing the shortest paths from the starting point to the neighborhood of the target object.
- `shortest_path_length`: shortest path length from source to that target.

# Quick Start



[![Watch the video](https://github.com/JiMa25/DOZE-Dataset/blob/main/assets/DOZE_full.jpeg)](https://youtu.be/vPuWM7ADxWc)



## Environment Setup

To set up the environment, follow these steps:
```
updating...
```
## Start example
```
cd scripts
python example.py
```


# Citation

```
@article{ma2024doze,
      title={DOZE: A Dataset for Open-Vocabulary Zero-Shot Object Navigation in Dynamic Environments},
      author={Ma, Ji and Dai, Hongming and Mu, Yao and Wu, Pengying and Wang, Hao and Chi, Xiaowei and Fei, Yang and Zhang, Shanghang and Liu, Chang},
      journal={arXiv preprint arXiv:2402.19007},
      year={2024}
}
```