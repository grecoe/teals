from support import ISolver, SqlDbDataStore, AzureStorageDataStore, DummySolver

import sys
import os

attempts=1
found=False
cur_path = os.getcwd()

while not found:
    if os.path.exists(os.path.join(cur_path, 'src')):
        sys.path.append(os.path.join(cur_path, 'src'))
        found = True
    cur_path = os.path.split(cur_path)[0]
    if attempts >= 3:
        break
    attempts += 1

from injection import ObjectFactory
from injection.exceptions import (
    FactoryArgCountException,
    FactoryException,
    FactoryMissingArgException
)

"""
    NEW singleton registry

    If a contained type for injection needs props to it's constructor that are not in 
    the singleton registry, you must create before calling generat_with_targets

    Calling generate or generate_with_targets for a singleton...if a singleton of that
    type already exists that's what you get back and any targets or construction params
    are ignored. You get what's already created. 

    If you have 2 possible injection targets that derive the same class and use the 
    simplified generate() you will get back whichever target was create first. In that
    case you must use generate_with_targets if you want more specificity.
"""
def test_basic_singleton():
    injection_factory = ObjectFactory()

    """
    Register a singleton by providing an instance of the singleton you want. 

    Can then retrieve the instance.
    """
    asd = AzureStorageDataStore("conn_str")
    injection_factory.register_singleton(asd)
    asd = injection_factory.get_singleton(AzureStorageDataStore)
    assert(asd != None)

    """
    Generate a singleton. The DummySolver expectes an IDataStore instsance which
    it will retrieve from the internal singleton registry.

    Also takes in the additional DummySolver construction (__init__) parameters
    which will also be inserted. 
    """
    solver = injection_factory.generate(DummySolver, True, {"store_query" : "Basic Query"})
    assert(solver != None)
    assert(isinstance(solver.datastore, AzureStorageDataStore))

    """
    Validate that we can get the singleton instance back.
    """
    solver = injection_factory.get_singleton(DummySolver)
    assert(solver != None)

    """
    Unregister the singleton and verify that it's not present anymore. We will 
    be down to the first singleton only.
    """
    injection_factory.unregister_singleton(DummySolver)
    solver = injection_factory.get_singleton(DummySolver)
    assert(solver == None)
    assert(len(injection_factory.singleton_registry) == 1)

def tests_advanced_singleton():
    injection_factory = ObjectFactory()

    """
    Regsiter two singletons, make sure we have both.
    """
    injection_factory.register_singleton(AzureStorageDataStore("conn_str"))
    injection_factory.register_singleton(SqlDbDataStore("svr", "usr", "crd"))
    assert(len(injection_factory.singleton_registry) == 2)

    """
    Generate a singleton DummySolver using the SqlDataStore
    """
    solver = injection_factory.generate_with_targets(DummySolver, True, [SqlDbDataStore], {"store_query" : "SQL STATEMENT"})
    assert(solver != None)
    assert(isinstance(solver.datastore, SqlDbDataStore))
    assert(len(injection_factory.singleton_registry) == 3)

    """
    Generating another DummySolver singleton actually returns the one that was already
    created, ignoring any additional parameters passed in.
    """
    solver = injection_factory.generate_with_targets(DummySolver, True, [AzureStorageDataStore], {"store_query" : "SQL STATEMENT"})
    assert(solver != None)
    assert(isinstance(solver.datastore, SqlDbDataStore))
    assert(len(injection_factory.singleton_registry) == 3)

    """
    Generating another DummySolver withoug singleton will generate another instance
    but not actually store it in the registry.
    """
    solver = injection_factory.generate_with_targets(DummySolver, False, [AzureStorageDataStore], {"store_query" : "SQL STATEMENT"})
    assert(solver != None)
    assert(isinstance(solver.datastore, AzureStorageDataStore))
    assert(len(injection_factory.singleton_registry) == 3)

def test_construction_params():
    injection_factory = ObjectFactory()

    injection_factory.register_construction_props(
        AzureStorageDataStore, 
        {"connection_string":"test_conn_string"}
        )

    stg = injection_factory.generate(AzureStorageDataStore, False, None)
    assert(stg != None)
    assert(len(injection_factory.singleton_registry) == 0)

def test_exceptions():
    injection_factory = ObjectFactory()

    try:
        stg = injection_factory.generate(AzureStorageDataStore, False, None)
    except Exception as ex:
        assert( isinstance(ex, FactoryMissingArgException))
        print(str(ex))

