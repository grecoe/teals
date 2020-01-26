# Intro to Computer Science (Python)
<sub>Dan Grecoe - A Microsoft Employee </sub>

This repo was put together for my first teaching experience with [Teals](https://www.microsoft.com/en-us/teals/about) with  Mr. Norton from [Essex North Shore](https://essexnorthshore.org/). 

This repository is meant to help beginner Computer Science students with Python.  

## Contents

|Name|Type|Content|
|----------|-------------|-------------|
|0_python|Directory|Introduction to basic Python programming structures and general programming.|
|1_practice|Directory|Some practice scripts for more complex Python concepts.|
|2_programs|Directory|Contains example programs using concepts covered in class. Other programs are added for the student to learn if they choose to.|
|3_quiz|Directory|Python scripts that test the student on their knowledge on particular topics covered in class. <br><br>This is a work in progress and the code inside will likely not make sense to the beginner student.|
|4_advanced|Directory|Advanced Python toopics that are not covered in the intro class, but can be useful for more advanced students (or for when I forget how to do something!).|
|README.md|file|This file you are reading right now.|

## Getting code locally

1. Create a directory on your computer. Name it anything you want, but make sure you remember it. 
2. Open a command prompt, bash, or Powershell.
3. Use the change directory (cd) command to point to the directory you created.
    - Example: `cd c:\teals`
4. Issue the following command in whatever prompt you used to create the directory.
    - `git clone https://github.com/grecoe/teals.git`
    
## Updating code locally

1. Go to the directory you cloned the repo on the command line.
2. Type the command git pull

## Using this repository
This repository attempts to organize the learning of the Python programming language. 

Starting in 0_python, students can learn the basic building blocks of the language. 

## Prerequisites
To make use of this repository it is recommended that the students have the ability to run the Python code on their own machines. It is possible, of course, to use online Python tools as well, but having the code locally means you can work on your Python skills without having to have any external connection.

1. Install [Python 3.5 or higher](https://www.python.org/downloads/)
2. Install [Visual Studio Code](https://code.visualstudio.com/download) (NOTE: This will run on Windows, Mac or Linux)
3. Clone this repository to your local machine. Note the directory in which the code is downloaded to.
4. Open Visual Studio Code and from the file menu, select Open Folder choosing the folder in which you downloaded this repository to. 

### Running the code
In Visual Studio Code you will have a list of files to the left and two panes on the right. The top pane being the code (or whatever) file you are looking at, the bottom having a multi tabbed view with one of them being the terminal. 

Change a directory and run a file by typing in the terminal window
```
cd 0_python
python 00_parameters.py
```

To vew the conents of the file, navigate to teh file in the left pane. 
