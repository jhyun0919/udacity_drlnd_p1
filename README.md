This project is one of the projects from [Udacity Deep Reinforcement Learning Nano-degree](https://github.com/udacity/deep-reinforcement-learning).

Following is the process and results I have done.

---

# Project Details

![](https://user-images.githubusercontent.com/10624937/42135619-d90f2f28-7d12-11e8-8823-82b970a54d7e.gif)

## The environment

In square world, an agent navigate and collect bananas(yellow and blue).  

The purpose of this project is training an agent to collect yellow bananas as many as possible while avoiding blue ones.
A reward of +1 is provided for collecting a yellow banana, -1 is provided for collecting blue one.

* State spcace: 37 dimensions
* Number of agents: 1
* Number of actions: 4 (move forward and backward, turn right and left)


**The agent must get an average score of +13 over 100 consecutive episodes**


# Getting Started

## Step 1: Clone the Repository

To clone this git repository, put a following commandline.

```
$ git clone https://github.com/jhyun0919/udacity_drlnd_p1.git
```


## Step 2: Download the Unity Environment

For this project, you need to download the Unity Environment from one ot the links below.

* [Linux](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana_Linux.zip)
* [Linux (headliss ver.)](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana_Linux_NoVis.zip)
* [OSX](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana.app.zip)
* [Windows (32-bit)](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana_Windows_x86.zip)
* [Windows (64-bit)](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana_Windows_x86_64.zip)

After download it, you need to place the file in the root directory of this project repository.

## Step 3: Set virtual environment for this project

The project dependency is listed in [requirements.txt]().  
The dependency can be met with the following command:

```
$ pip install -r requirements.txt
```

# Instructions

You can check out about the design & results of the experiment on this project in [Report.ipynb]().

