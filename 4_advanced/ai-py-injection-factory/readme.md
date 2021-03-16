# Injection Factory

This package contains a Python version of a dependency injector. To use it there are a couple of design issues that first must be met.

## Class Declaration
When you declare a class and you have parameters in the init funciton, they <b>must</b> use typing, i.e.

```python
class SqlDbDataStore(IDataStore):
    def __init__(self, server : str, user : str, cred : str):
        ...
```

When you declare a class that is to use injection you include the class/interface type that is going to be injected.

```python
class DummySolver(ISolver):
    def __init__(self, data_store : IDataStore, store_query : str):
```

## Dependency Injection
From the two examples above the SqlDbDataStore is an IDataStore and the DummySolver expects an IDataStore.The steps needed are:

1. Create an instance of SqlDbDataStore to be injected to the DummySolver, it must be a registered singleton.
```python
injection_factory = ObjectFactory()

# This 
injection_factory.register_singleton(SqlDbDataStore("svr", "usr", "crd"))
# or this
injection_factory.register_construction_props(
            SqlDbDataStore, 
            {
                "server":"svr",
                "user" : "usr",
                "cred" : "crd"
            }
        )
stg = injection_factory.generate(SqlDbDataStore, True, None)
```
2. Create an instance of the solver. You can use the flag to determine if it should be added as a registered singleton or not. In this case, we are saying True (yes, singleton please)
```python
# This
solver = injection_factory.generate(DummySolver, True, None,{"store_query" : "Basic Query"})
# or this
injection_factory.register_construction_props(
            DummySolver, 
            {
                "store_query":"Basic Query"
            }
        )
solver = injection_factory.generate(DummySolver, True, None, None)        
```
3. Now anytime you need that solver with that data store, you can just ask for it
```python
solver = injection_factory.get_singleton(DummySolver)        
```

## More information
To see more information read the source at 
- src/injection/factory.py

Or the unit tests at
- tests/test_fact.py