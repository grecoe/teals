# Testing

This part of the repository is for instructors to create automated tests for Python files submitted by students. 

June 3, 2020 : There is one program here that will test a python file assuming it has functions to be tested.

To test the app in this location:

```
python .\autotest.py -mod student -config hw1.json
```

## autotest

### autotest.py
The testing application. It requires two pieces of information that can be provided by a parameter, or will be requested when run:

|Parameter|Purpose|
|---------|-------|
|-mod|The name of the student module to be tested. This will the name of a python file (without the .py extension) in the current directory.|
|-config|The JSON definition file of the tests to be run.|

### hw1.json
This file is an example of the needed JSON definition file for the tests to run on the student module (-mod). 

It is broken down as shown below. Each test has a list of functions it is to test. 

A function can take 0 or more parameters in it's params dictionary that must be in the order in which the function expects them. 

The result is also part of the function definition here so that the return value can be validated.

```
{
    "Name" : "First Homework Assignment Test",
    "Functions" : [
        {
            "name" : "multiply",
            "params" : {
                "x" : 20,
                "y" : 10
            },
            "expected_output" : 200
        },
        {
            "name" : "noop",
            "params" : {
            },
            "expected_output" : null
        }

    ]
}
```

<b>NOTE</b> A function that returns None is defined with expected output as null in JSON.

### student.py
This is an example of a student program that is submitted to be tested by the file hw1.json. 

Note that the doc string at the top of this file identifies the student name and is required. 