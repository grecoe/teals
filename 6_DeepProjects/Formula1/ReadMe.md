# Formula 1 Application

Explore Formula 1 Data from 1950 - 2017

Data Provided by kaggle.com : https://www.kaggle.com/cjgdev/formula-1-race-data-19502017

This project allows you to program interesting information about Formula 1 over many years. 

This application combines several ideas and strategies to create an application to review the Formula One data from Kaggle utilizing the tools in the mutli_command_utils directory. You should start with that readme.md file to really understand what is going on.  

It is a command line application that takes multiple level commmands, such as 

<br>
get driver stats -f Ayrton -l Senna
<br>
get driver stats -i 102
<br>
list drivers -y 2015
<br>
list drivers -l Andretti
<br>
list drivers -q nationality=Brazilian

# Structuring of the program
These sections are organized in a way to help you understand how the program functions and the important topics.

## 1. Obtaining Data
The data set that is used for this example is a Kaggle dataset that covers the Formula One World Championship statistics from 1950-2017. 

It is broken down into several CSV files. To make sense of that data, you need to read in the CSV data and be able to interact and search it. 

Specific readers for each of the data files are required to access and merge data to make the applicaiton useful in any way. 

|Directory|File|Purpose|
|---------|----|-------|
|Formula1/f1_data_readers|*.py|Specific implementations of the DataFile class wrapping individual CSV files from the Kaggle dataset.<br><br>> These will work assuming you have created a directory called data/ and placed the Kaggle data set into that directory. |

<b>NOTE</b> If there is a dataset that does not currently have an implementation in f1readers/ you will need to create it. 

## 2. Application Functions and Helpers
To abstract away the reading and processing of the Formula One data from the core application functionality, the readers are wrapped in IFunction instances which will do all of the actual heavy lifting during execution. 

IFunction defines a contract that must be adhered to for proper program functionality. 

The files which implement the IFunctions for the Formula One Data are:

|Directory|File|Purpose|
|---------|----|-------|
|Formula1/f1_functions|constants.py|Contains a class called F1DataConstants which contains only static fields for the dataset names we want to load.<br><br>These constants are used when setting up the dataset dictionary to pass to the base class IFunction so that our Formula One functions will understand the dataset dictionary to access relevant data.| 
|Formula1/f1_functions|*.py|Any other specific examples, if provided.|

## 3. Application Implementation
The application is implemented using the MultiCommandApp class. The essential steps that are performed are:

1. Run python f1app.py
2. First sets the path to the 06_DeepProjects directory so that Python will know how to load up the utilities from multi_command_utils library. 
2. Build up the data files dictionary that will be passed to each IFunction implementation. 
3. Define the program menu (app_functions)
4. Create an instance of MultiCommandApp using the dictionary from 3. above and call run(). 


### Things you could try....
- New DataFile implementations, if you wish. If you do not use data files, that parameter to the base IFunction can be None....the base class never actually accesses the data files. 
- A new app_functions dictionary defining the functionlity and flow you desire for your application. 

HAVE FUN!
