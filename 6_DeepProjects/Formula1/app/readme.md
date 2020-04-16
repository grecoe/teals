# Formula One Application
This application combines several ideas and strategies to create an application to review the Formula One data from Kaggle. 

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

The files described in this section provide the ability to load and make available data from specific files (read below) to enable functionality in the application.  

<b>NOTE</b> As with the other examples in this repository, the Kaggle dataset is extracted into a directory called data/ as a peer directory to this app/ directory.

|Directory|File|Purpose|
|---------|----|-------|
|Formula1/readers|base.py|Contains a class called DataFile that other, specifc, data readers derive from.<br><br>This class is manage loading CSV data from a provided directory and file name that.<br><br>This base reader functionality exposes file headers, data rows and searching by column header to retrieve an entire column. |

## 2. Application Functions and Helpers
To abstract away the reading and processing of the Formula One data from the core application functionality, certain functionality has been created to support this in the form of classes. 

Essentially, this functionilty consists helper classes that allow you to create and extend the application quite easily. The two files you need to be aware of are:

|Directory|File|Purpose|
|---------|----|-------|
|Formula1/app/utils|menuutils.py|Contains a class called MenuUtils. As a caller, you provide your application dictionary (described below) to the static call MenuUtils.display_menu_help(app_functions).<br><br>This will present the user with the application menu and the selections that they can make to interact with your application.|
|Formula1/app/utils|interface.py|Contains a class called IFunction. This is the base class of any real processing function you want to implement in your program. The menuutils.py class understands this base class as does the main functionality in the f1.py file.|

### 2.1 Menus

The application menu is comprised of a dictionary that
1. Has strings as keys and is organized to define the commands that a user will enter to perform actions in your program. 
2. Has node values that are either:
    - An IFunction implementation. These can and do accept additional arguments to define the function execution. 
    - A standard python function. These cannot accept any additional arguments. 

This menu structure can be re-used in any application you wish as the implementation of it is separated, through code, from any specific Forumula One activity. 

A menu would be described in your code as follows (and you can navigate to f1.py to see a bigger definition)

```
app_functions = {
    "get" : {
        "stats" : {
            "constructor" : DummyFunction(dataset),
            "driver" : DummyFunction(dataset)
        }
    },
    "quit" : quit
}
```

In this case the user would be able, from the command line, to enter:

```
> get stats constructor ->  Calling DummyFunction with 
                            potentially more arguments
> get stats driver      ->  Calling DummyFunction with 
                            potentially more arguments
> quit                  ->  Calls pythons quit() method
```

### 2.2 Functions
As noted already, an implementation of IFunction can be used as a leaf node in an application dictionary. 

IFunction defines a contract that must be adhered to for proper program functionality. There are several examples of this, with the simplest located at app/f1functions/dummy.py

The interface, or base class, supplies significant functionality on your behalf. The following definition of the class will give you more insight as to what it's doing for you and what you must ultimately provide in your own implementation. 

|Function|Parameters|Description|
|--------|---------------------|-------|
|__init__()|datasets<br>acceptable_arguments|Initializes the base class with the datasets that should be available and the arguments that are acceptable for this instances.<br><br><b>datasets:</b>This is a dictionary with keys (of whatever you want them to be) and values that are instances of DataFile. Of course, you can do what you want, but this is how the data files are then exposed to the deriving classes.<br><br><b>acceptable_arguments:</b>This is a list of the named tuple argument_definition that is defined in the interface.py file. This tells the class what parameters it will accept as well as those that would be required.<br><br><b>NOTE</b> Every instance of IFunction will, by default, get two additional acceptable parameters:<br>-h : Help<br>-q : query| 
|execute()|args|<b>This function must be defined in the deriving class. This is the function that will be called when the action is requested by the user</b><br><br><b>args:</b>A list of additional arguments that were passed to the command. Keep reading this class description as there are more functions that help you manage arguments.|
|get_arguments()|None|Returns all of the arguments this function will accept in a comma separated list which is used at the program level help command.|
|get_help()|indent<br>command_list = None|Prints out the help for this function.<br><br><b>indent:</b>Indentation for the output of the menu.<br><br><b>command_list:</b>If provided, the string list items are joined by a space and used in the menu output.|
|_parse_execute_arguments()|args|Provides the functionality to split out the additional arguments passed for the command into an array in which the key is the argument type (i.e. -f) and the value is a string representing all fo the data that was provided for a specific arg.<br><br>The funciton should be called from within your implementation of execute() to collect the arguments dictionary<br><br>Internally the function validates the arguments and will emit an exception if:<br><br>1. A required argument is missing<br><br>2. An unexpected argument is found.<br><br>If help (-h) is passed, argument validation is not performed.<br><br><b>args:</b> Any additional information for the command that the user has entered.|
|_parse_query()|query_string|This function is used internal to the _parse_execute_arguments function.<br><br>A query is comprised of a string in the form:<br><br>key=value;key2=value2<br><br>Where key is a column name from the CSV file and value is a value in that column to match.<br><br>You can pass 1 or more key/value pairs. If more than one they must be separated by a semi-colon.<br><br><b>query_string:</b>This is the string entered in for the command after the '-q' query argument.| 


# Formula One Implementations
The above sections desribed the DataFile reader class for CSV files as well as the MenuUtils and IFunction classes that are used as the basis of this application. 

Those classes can be used for, really, any type of program you want to write. For this example, using the Forumula One data, specific implementations of DataFile and IFunction were required. 

## 1. DataFile Implementations
Specific readers for each of the data files are required to access and merge data to make the applicaiton useful in any way. 

|Directory|File|Purpose|
|---------|----|-------|
|Formula1/f1readers|*.py|Specific implementations of the DataFile class wrapping individual CSV files from the Kaggle dataset.<br><br>> These will work assuming you have created a directory called data/ and placed the Kaggle data set into that directory. |

<b>NOTE</b> If there is a dataset that does not currently have an implementation in f1readers/ you will need to create it. 

## 2. IFunction Implementations
Specific functions are also required to perform actions on the datasets.

Looking through these files you'll get a better understanding on how to define arguments, process arguments in execute(), and generally how it all comes together.

|Directory|File|Purpose|
|---------|----|-------|
|Formula1/app/f1functions|constants.py|Contains a class called F1DataConstants which contains only static fields for the dataset names we want to load.<br><br>These constants are used when setting up the dataset dictionary to pass to the base class IFunction so that our Formula One functions will understand the dataset dictionary to access relevant data.| 
|Formula1/app/f1functions|dummy.py|A clean example on how to derive from IFunction and implement the execute() function.|
|Formula1/app/f1functions|*.py|Any other specific examples, if provided.|

<b>NOTE:</b> Formula1/app/functions/driver_stats.py implements the same functionality as the abstract.py and starter.py but wrapped in an IFunction. It's still as messy as ever :) So feel free to clean it!

## 3. Application Implementation
By now (because you hopefully read the above information), you have an understanding of the base helper classes and the locations of the specific implementations for this program. 

With that, we can now delve into our application specific implementation for the Formula One appliation. 

The application can be found in this file:

Formula1/app/f1.py

This file pulls it all together. The important steps here are:

1. Build up the data files dictionary that will be passed to each IFunction implementation. 
2. Define the program menu (app_functions)
3. Put a loop together that can accept user input, then walk through it one word at a time to figure out if there is a function at the end that needs to be called. 

<b>NOTE:</b>The main program loop could be re-used in other applications you want to define. The functionality will NOT change. The only changes you really need are:

- New DataFile implementations, if you wish. If you do not use data files, that parameter to the base IFunction can be None....the base class never actually accesses the data files. 
- A new app_functions dictionary defining the functionlity and flow you desire for your application. 

HAVE FUN!