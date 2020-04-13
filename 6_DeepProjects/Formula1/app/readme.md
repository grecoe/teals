# Formula One Application
This application combines several ideas and strategies to create an application to review the Formula One data from Kaggle. 

It is a command line application that takes multiple level commmands, such as 

show driver stats -f Ayrton -l Senna
show constructor stats -n McLaren -y 1986

## Structuring of the program
These sections are organized in a way to help you understand how the program functions and the important topics.

### Obtaining Data
The data provided in the data set is all in CSV format. However, the base CSV reader in Python has issues with this data and a customize reader was created.  

As with the other examples in this repository, the kaggle dataset is extracted into a directory called data/ as a peer directory to this app/ directory.

|Directory|File|Purpose|
|---------|----|-------|
|Formula1/readers|base.py|Contains a class called DataFile that other, specifc, data readers derive from.<br><br>This class is provided a directory and file that contains CSV data and reads that data into memory.<br><br>Further, the class provides base functionality, including searching by columns data, for accessing CSV data.|
|Formula1/custom|*.py|Specific implementations for the data files provided in the Kaggle dataset which all derive from readers/base/DataFile. These implementations feed in the data directory and a specific CSV file from that data.|

<b>NOTE</b> If there is a dataset that does not currently have an implementation in custom/ you will need to create it. It's also important that you understand how to use these files as you move forward in the program. 

### Functions and functionality
All of the functionality in this application comes from an instance of an IFunction class instance (more to come). These instances provide information in which the function can define it's own help, but also execute a particular piece of funcitonality with or without additional arguments. 

For example:
- No arguments: > help
- Arguments : show driver stats -f Ayrton -l Senna

It is important to understand how these are structured and you should become very familiar with the following two files:

|Directory|File|Purpose|
|---------|----|-------|
|Formula1/app/functions|IFunction.py|Base class for every function that will be exposed through the application.<br><br>The template class provides the funtionality for containing the arguments definitions and data sets.<br><br>For arguments, argument parsing and argument validation is provided for any derived class in a clean way.| 
|Formula1/app/functions|dummy.py|A clean example on how to derive from IFunction.|
|Formula1/app/functions|*.py|Any other specific examples, if provided.|

<b>NOTE:</b> Formula1/app/functions/driver_stats.py implements the same functionality as the abstract.py and starter.py but wrapped in an IFunction. It's still as messy as ever :) So feel free to clean it!

### Program Flow - Menus
The program requires that a dictionary for commands be used to drive the flow of the program. 

The dictionary lays out the flow of commands as string keys. End nodes are either:
1. An instance of IFunction (derived class)
2. Some standard function, like quit()

Example:
Support for three commands:

get stats constructor
get stats driver
quit

Would be defined as:

```
app_functions = {
    "get" : {
        "stats" : {
            "constructor" : DummyFunction(f1_datasets),
            "driver" : DummyFunction(f1_datasets)
        }
    },
    "quit" : quit
}
```
Functionality to support showing the menu with the help options is provided for you. 

|Directory|File|Purpose|
|---------|----|-------|
|Formula1/app/utils|menuutils.py|Contains a class called MenuUtils. As a caller, you provide your application dictionary (section above) to the static call MenuUtils.display_menu_help(app_functions)|

### Application Implementation
Now that you understand the structures used to build the applicaiton, now comes the application. This file is:

Formula1/app/f1.py

This file pulls it all together. The important steps here are:

1. Build up the data files dictionary that will be passed to each IFunction implementation. 
2. Define the program menu (app_functions)
3. Put a loop together that can accept user input, then walk through it one word at a time to figure out if there is a function at the end that needs to be called. 