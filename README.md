# Lawrence Detroit Lions Bingo Generator

## Overview
This repository creates a number of custom bingo sheets based on all the things Lawrence Linneburg may say or do during a Detroit Lions game. Have fun!

## Setup

### Requirements
* Python3.7 or later

### Clone this repo
```shell
git clone git@github.com:JoshLinneburg/lawrence-lions-bingo.git
```

### Create a virtual environment in the project root
```shell
python -m venv env
```
### Activate the virtual environment<br>
#### For Mac/Linux users:
```shell
source ./env/bin/activate
```

#### For Windows users:
```shell
.\env\Scripts\activate
```

### Install the necessary libraries
```shell
pip install -r requirements.txt
```

## How To Run
At the moment, the repo uses a single `run.py` file with a hard-coded list of contestants, but you can change this yourself.<br>
CLI options and better user experience is still TBD as this was an afternoon project.

### Run the program
```shell
python run.py
```
