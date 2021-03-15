# Parameter Validation
When developing software, one of the lowest hanging fruit items you can choose to manage is validation of parameters being passed to your methods.

This is true whether the method is free standing (outside a class) or contained within a class.

This repo has a decorator class that can be used in both cases.

## Example 1 - Standalone Function with defined arguments

Standalone method with arguments
```python
@ParameterValidator((int, False), (str, False), (list, True))
def myfunc(num, str, list):
    print("Hello from standalone function")
```
Test it using splatting and with set parameters
```python
# Splatting
single_args = [1, "hey", None]
print("Standalone Args Splatting -")
myfunc(*single_args)

# Standard call
print("Standalone Args Standard -")
myfunc(1, "hey", None)
```

# Example 2 - Standalone function using kwargs
Function
```python
# Test standalone method with kwargs
@ParameterValidator(age=(int, False), name=(str, False), addresses=(list, True))
def mykwfunc(**kwargs):
    print("Hello from kwargs standalone function")
```
And test this
```python
print("Standalone Kwargs Standard -")
mykwfunc(age=25, name="Fred Jones")
```

# Example 3 - Class with both types of functions
Class definition:
```python
class TestDecorator:
    def __init__(self):
        pass

    @ParameterValidator((int, False), (str, False), (list, True))
    def myfunc(self, num: int, str: str, list: typing.List[object]):
        print("Hello from class method")

    @ParameterValidator(age=(int, False), name=(str, False), addresses=(list, True))
    def mykwfunc(self, **kwargs):
        print("Hello from kwargs class function")
```
And finally, test the class
```python
td = TestDecorator()
print("Class Args Standard -")
td.myfunc(1, "str", [])
print("Class Kwargs Standard -")
td.mykwfunc(age=25, name="Fred Jones")
```