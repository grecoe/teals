import typing
from src import ISolver, SqlDbDataStore, AzureStorageDataStore, DummySolver


def test_solver_di(solver : ISolver):
    assert(isinstance(solver, ISolver))

    print("\nRunning Solver, run results below...")
    res = solver.run()
    for k in res:
        print(k, '-', res[k])


"""
External to any logic, we know how to create the different
IDataStore types. 
"""
stg_option = [
    AzureStorageDataStore("conn_str"),
    SqlDbDataStore("svr", "usr", "cred")
]

"""
Similarly, we know how to create the solvers, and we inject
anything that it will need. 

In this case it requires an IDataStore and a query string.

Lets pass both to the DummySolver class so we can see the output
change from one store to the other. 
"""
for stg in stg_option:
    test_solver_di(DummySolver(stg, str(type(stg))))
