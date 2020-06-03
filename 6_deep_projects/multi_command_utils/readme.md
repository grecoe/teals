# Multi Command Utils

This directory contains several helper files to quickly and easily create a python command line program that :

- A simple way to define a data file reader (CSV) that encapsulates some searchign functionality.
- Create a command line program that accepts multi word commands
    - Commands can be either functions or a specific type of class instance
    - Provides default functionality of
        - Verifying parameters to functions
        - help, quit and clear screen functions

# Structuring of the program
These sections are organized in a way to help you understand how the different parts of this folder can help you build a robust application. 

## 1. Obtaining Data
If your application needs data, a useful utility has been put together to be able to load CSV files.

CSV files can be thought of as a sort of table with rows and columns. 

In one of hte examples (03_FormulaOne), it utilizes several CSV data files to be build useful data insights.

You can use the DataFile class directly, or derive (as the Formula One example does) a new class from DataFile. 

|Directory|File|Purpose|
|---------|----|-------|
|multi_command_utils|data_file.py|Contains a class called DataFile that other, specifc, data readers derive from.<br><br>This class is manage loading CSV data from a provided directory and file name that.<br><br>This base reader functionality exposes file headers, data rows and searching by column header to retrieve an entire column. |

## 2. Application Functions and Helpers
The flow of an application is defined by a dictionary (see menuutils.py below) that is built using string keys and functions or implementations of a class IFunction (see interface.py below). 

|Directory|File|Purpose|
|---------|----|-------|
|multi_command_utils|menuutils.py|Contains a class called MenuUtils. As a caller, you provide your application dictionary (described below) to the static call MenuUtils.display_menu_help(app_functions).<br><br>This will present the user with the application menu and the selections that they can make to interact with your application.|
|multi_command_utils|interface.py|Contains a class called IFunction. This is the base class of any real processing function you want to implement in your program. The menuutils.py class understands this base class as does the main appliation loop in multi_command_applicaton.py/MultiCommandApp.|
|multi_command_utils|multi_command_applicaton.py|Contains a class called MultiCommandApp. This class has a single function for you to call - run().<br><br> When seeded with a menu dictionary, it will execute your application without a need for you to modify the code.|

### 2.1 Menus

The application menu is comprised of a dictionary that
1. Has strings as keys and is organized to define the commands that a user will enter to perform actions in your program. 
2. Has node values that are either:
    - An IFunction implementation. These can and do accept additional arguments to define the function execution. 
    - A standard python function. These cannot accept any additional arguments. 

This menu structure can be re-used in any application you wish as the implementation of it is separated, through code, from any specific program activity. However, if you use the MultiCommandApp, the use of the menu is abstracted away from you.

A menu would be described in your code as follows:

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

IFunction defines a contract that must be adhered to for proper program functionality. There are several examples of this, with the simplest located at multi_command_utils/interface_dummy.py

The interface, or base class, supplies significant functionality on your behalf. The following definition of the class will give you more insight as to what it's doing for you and what you must ultimately provide in your own implementation. 

|Function|Parameters|Description|
|--------|---------------------|-------|
|__init__()|datasets<br>acceptable_arguments|Initializes the base class with the datasets that should be available and the arguments that are acceptable for this instances.<br><br><b>datasets:</b>This is a dictionary with keys (of whatever you want them to be) and values that are instances of DataFile. Of course, you can do what you want, but this is how the data files are then exposed to the deriving classes.<br><br><b>acceptable_arguments:</b>This is a list of the named tuple argument_definition that is defined in the interface.py file. This tells the class what parameters it will accept as well as those that would be required.<br><br><b>NOTE</b> Every instance of IFunction will, by default, get two additional acceptable parameters:<br>-h : Help<br>-q : query| 
|execute()|args|<b>This function must be defined in the deriving class. This is the function that will be called when the action is requested by the user</b><br><br><b>args:</b>A list of additional arguments that were passed to the command. Keep reading this class description as there are more functions that help you manage arguments.|
|get_arguments()|None|Returns all of the arguments this function will accept in a comma separated list which is used at the program level help command.|
|get_help()|indent<br>command_list = None|Prints out the help for this function.<br><br><b>indent:</b>Indentation for the output of the menu.<br><br><b>command_list:</b>If provided, the string list items are joined by a space and used in the menu output.|
|_parse_execute_arguments()|args|Provides the functionality to split out the additional arguments passed for the command into an array in which the key is the argument type (i.e. -f) and the value is a string representing all fo the data that was provided for a specific arg.<br><br>The funciton should be called from within your implementation of execute() to collect the arguments dictionary<br><br>Internally the function validates the arguments and will emit an exception if:<br><br>1. A required argument is missing<br><br>2. An unexpected argument is found.<br><br>If help (-h) is passed, argument validation is not performed.<br><br><b>args:</b> Any additional information for the command that the user has entered.|
|_parse_query()|query_string|This function is used internal to the _parse_execute_arguments function.<br><br>A query is comprised of a string in the form:<br><br>key=value;key2=value2<br><br>Where key is a column name from the CSV file and value is a value in that column to match.<br><br>You can pass 1 or more key/value pairs. If more than one they must be separated by a semi-colon.<br><br><b>query_string:</b>This is the string entered in for the command after the '-q' query argument.| 


### 2.3 Application Class
As noted already, the MultiCommandApp class encapsulates the execution of your multi command application when seeded with a dictionary that meets the requirements. 

Additional notes on this class:
- The constructor will provide quit/clear/help functionality by name if you do not provide it. 
- Call run() to start your program. 
