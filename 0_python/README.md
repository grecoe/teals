# Python
<sub>Dan Grecoe - A Microsoft Employee </sub>

Python is a computer coding language that is widely used in the IT and software industries. 

Really, anywhere people are working on computers you will find the Python language. 

Python is an interpreted language. That means there is a larger program that reads a Python file (script) and executes the commands. Unlike C, C++, etc, there are no intermediate steps such as compiling your Python code before you run it.  

Python can be run in one of two ways, but first you MUST install it on your computer. 

1. From the command line, just type the word 'python'. This will start the interpreter and you can then start entering in python commands. 
2. Executing a python script (which is really just a text file with the extension '.py')

## Python Language
Like learning any language, you need to understand the words in that language and start using them in "sentences". 

So the first thing to know is, what are the words in the language? Python has a list of reserved keywords. You can find these by starting Python on the command line (as explained above) and type these commands in:

```
import keyword
print(keyword.kwlist)
```

This will be the full list of reserved words in the Python language. 

Many, but not all, of those keywords are explained in the files contained in this folder. 

### Built in functions
Python has a number of built in functions. These are pieces of code that are provided in the standard distrubution of the language and are available to you. 

The full list of built in functions can be found [here](https://docs.python.org/3/library/functions.html)

As a beginner, you will use a subset of these built in functions, but like the reserved keywords, not all will be included in the introduction to the Python language. 

There are, however, many websites that go deeply into describing them and how to use them. 

Primarily, for this introduction you will become familiar with the following built in functions.

NOTE: Don't worry about understanding these immediately, you will be introduced to them as we move through the content. 

|Function|Use|
|----------|------------|
|bool(arg)|Construct a boolean value using the provided function argument, which is typically a string.|
|int(arg)|Construct an integer value using the provided function argument. This can be a string or any numeric value.|
|float(arg)|Construct a boolean value using the provided function argument.This can be a string or any numeric value.|
|str(arg)|Construct a string value of the provided function argument.|
|input(prompt)|On the command line print the string value 'prompt' and collect typed in data the user provides until they hit the enter key.|
|len(arg)|Return the number of items in arg. This implies that arg is a sequence of some kind. For example a string is a sequence of characters.|
|[range()](https://docs.python.org/3/library/functions.html#func-range)|Return a sequence of numbers. This is a little more complex than the previous functions, so click on the link to get a description.|
|type(arg)|Retrieves the type information of a varaible, function or other structure. This can come in handy as Python is very loosely typed.|
|None|This is a special type in Python. In other languages this would be called null/NULL and indicates that a variable holds no value.|

## Index
This folder contains tutorials on things that we are covering in class. Basically the building blocks you will need to write and understand basic python scripts. 

The files are numbered to keep them in some sort of order in which you can learn. Open them up, the comments guide you through it. 

|File|Description|
|--------|--------------|
|00_variables.py|Introduction to python variables.|
|01_boolean.py|Introduction to boolean values and boolean math.|
|02_casting.py|Introduction to casting values to different types. |
|03_comparisons.py|Introduction basic value comparisons. |
|04_input.py|Introduction to getting user input. |
|05_if.py|Introduction to the if statement.|
|06_while.py|Introduction to the while statement.|
|07_for.py|Introduction to the for statement.|
|08_list.py|Introduction to Python lists.|
|09_dictionary.py|Introduction to Python dictionaries, sometimes known as hash tables. |
|10_functions.py|Introduction to Python functions. |
|11_scope.py|Understanding the scope of a variable whether you are in a function or on the global scale, is important. This introduction to scope will give the reader a decent background. |
|12_file.py|Introduction to files.|

## Introduction To Python Structures
Use these files, in numeric order, to walk new Python students through the basic building blocks of the language. 

Building one upon the other, by the end of this section, students should have gained a strong understanding of basic python programming. 