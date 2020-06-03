# Deep Projects

<b>NOTE</b> This folder holds programs and utilities best suited for more advanced students as some of the techniques used here are fairly advanced. 

## Overview

Many times when learning a new language as a student you are creating command line programs, typically by starting out by taking in some basic information from a user and echo that same data back. 

As you progress, the programs become more complex. You have more commands or commands that mirror each other with minor changes. 

In this folder you will be introduced to some utilities that can make your life considerably easier. The utilities are generic in nature and you can re-use the code in many projects you may need to create. 

The content you should cover, <b>in order</b>, is as follows:

|Order|Directory|Content|
|---|---------|-------|
|1.|multi_command_utils|This folder contains the utilities mentioned above. It will be worth your time to read the readme.md file in that directory and understand what it says as these utilities are used in the remainder of the examples.|
|2.|MenuBasics|Introduction to using the utilities menuutils.py and multi_command_application.py in the multi_command_utils.<br><br>This uses standard Python functions tied to the program menu and is the easiest of the application examples to follow.|
|3.|MenuIFunction|Expands on MenuBasics and introduces the IFunction class (interface.py) to manage your application in a more abstract way.|
|4.|MenuShoppingCart|Expands on MenuIFunction to do some actual work by implementing the shopping cart exampel used in for loops review.|
|5.|FileData|Introduction to using the data (CSV) file reader. This is used extensively in the Formula1 project and if you are moving on to that, it's worth having a look at what you can do with that base class.|
|6.|Formula1|This is a much more complex example of using the different utilities. It reads (data provided) a bundle of CSV files provided by Kaggle.com, that contain information on the Formula One World Championship from 1950-2017.<br><br>It is HIGHLY recommended you work through the previous examples before you tackle this one.|