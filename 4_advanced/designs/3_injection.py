"""
    Dependency Injection (DI) and Inverson of Control (IOC) are two different topics that can be used
    synonymously depending on context. 

    DI is used to loosly couple objects/functionality and is typically accomplished through constructor
    parameters or through property setters. 

    IOC is a design principle in which flow is inverted via a framework. However, DI really is a version of 
    IOC as the control of construction, lifetime and functionality are inverted to injected objects. 
"""
import os

os.environ["API_KEY"] = "special_key"
os.environ["TIMEOUT"] = "3600"


"""
    EXAMPLE 1 - Tight coupling :
        In this case both AppClientTight and ServiceTight have external dependencies 
        that cannot change. 
"""
class ApiClientTight:

    def __init__(self):
        self.api_key = os.getenv('API_KEY')  # <-- dependency
        self.timeout = os.getenv('TIMEOUT')  # <-- dependency


class ServiceTight:

    def __init__(self):
        self.api_client = ApiClientTight()  # <-- dependency

# While creating a ServiceTight instance is straightforward, the cohesion between 
# the service and client, and client and environment are tightly coupled.
st = ServiceTight()
print(st.api_client.api_key)





"""
    EXAMPLE 2 - Loose coupling through injection
        In this case both AppClientLoose and ServiceLoose have no external dependencies 
        as they are provided through constructors.
"""
class ApiClientLoose:

    def __init__(self, key : str, timeout : int):
        self.api_key = key
        self.timeout = timeout


class ServiceLoose:

    def __init__(self, client : ApiClientLoose):
        self.api_client = client

# Creating a ServiceLoose instance is slightly more work in that all external 
# requirements are met in the controlling applicaiton instead of interally. 
# The service and client are both loosely coupled and settings/requirements 
# can be modified in the aplication without modifying the underlying implementations. 
sl = ServiceLoose( 
        ApiClientLoose(
            os.getenv('API_KEY'), 
            os.getenv('TIMEOUT'))
    )
print(sl.api_client.api_key)
