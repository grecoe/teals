# Full example

This is a full example to show how to pull these suggestions together into a cohesive collection of source code. 

Concepts covered:
- Core functionality contained within classes. 
- Interfaces and class derivation to make dependent classes more generic.
- Dependency injection
- Bonus : DI Factory

## Contents

|Folder|Contents|
|---------|---------|
|src/interfaces|Definition of interfaces to use. In this example an IDataStore and ISolver interface are defined.<br><br>These interfaces are VERY basic and used just for examples.|
|src/datastores|Implementations of the IDataStore interface.|
|src/solvers|Implementations of the ISolver interface.|
|src/exceptions|Customized Exceptions that can be raised when an error occurs.|
|.|app.py which is the file to run and test this out.<br><br>factory.py can effectively be ignored. It's a rudimentary run at creating a Dependency Injection library.|


### Output
When you run app.py the output will be:
```
Running Solver, run results below...
AzureStorageDataStore - <class 'src.datastores.storagestore.AzureStorageDataStore'>

Running Solver, run results below...
SqlDbDataStore - <class 'src.datastores.sqldbstore.SqlDbDataStore'>
```


# Using the factory
The factory.py file contains a rudimentary DI factory that can solve many DI object creation tasks for the developer. While this may not be fully production ready, it automates the injection process for the caller. 

```python
from src import ISolver, SqlDbDataStore, AzureStorageDataStore, DummySolver
from factory import DIFactory

di = DIFactory()
# First task is to either regster created objects OR seed any additional (or all)
# props needed to generate an object.

# Create an instance and register it. This will place an instance of AzureStorageDataStore
# in the internal register which will be used any time it is required for injection OR any
# time one of its derviations is called for.
di.register_object(AzureStorageDataStore("conn_str"))
solver = di.generate(DummySolver, {"store_query" : "Basic Query"})
res = solver.run()
print(res)
```
> Output 1: {'AzureStorageDataStore': 'Basic Query'}

```python
# A more complex but more flexible way
di = DIFactory()
# Register any additional (or all) constructor parameters for an object.
di.register_construction_props(AzureStorageDataStore, {"connection_string" : "storage_conn"} )
di.register_construction_props(SqlDbDataStore, {"server" : "sqlserver", "user" : "username", "cred" : "usercred"} )
di.register_construction_props(DummySolver, {"store_query" : "DI Query"} )

# Call generate with targets and tell it explicitly which specific type of 
# object you want injected in the constructor. 

# First run is to create the sovler with AzureStorageDataStore and use the interal construction
# props we already registered above. 
solver = di.generate_with_targets(DummySolver, [AzureStorageDataStore], None)
res = solver.run()
print(res)
```
> Output 2: {'AzureStorageDataStore': 'DI Query'}

```python
# Second run uses a different IDataStore (SqlDbDataStore) and a different store query which 
# will override whatever was already registered for this type of object. 
solver = di.generate_with_targets(DummySolver, [SqlDbDataStore], {"store_query" : "SQL STATEMENT"})
res = solver.run()
print(res)
```
> Output 3: {'SqlDbDataStore': 'SQL STATEMENT'}