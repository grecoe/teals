"""
    Interfaces help keep code generic. 
    
    When we start to look at dependency injection, the injection of objects should
    similarly be generic in that it recieves and interface type as opposed to a hard
    type. 

    This keeps coupling looser and in many cases reduces or removes any modifications 
    to more complex objects that consume them.  
     
    In languages such as C# creating an interface is straight forward and you cannot 
    instantiate one stand alone, it must be derived. 

    To accomplish something similar we use the ABC library as below
"""

from abc import ABC, abstractmethod

class IApiClient(ABC):
    """
    Interface definition for Python. The use of abstractmethod means 
    that this class cannot itself be instantiated but must be derived 
    to take on the shape of this interface.

    All abstract methods MUST be defined in the deriving class. 
    """

    # Using abstract methods prevents instantiation of this 
    # type on it's own, it must be derived.
    @abstractmethod
    def get(self, url: str) -> None:
        pass


class HttpClient(IApiClient):
    """
    Derivation of the IApiClient interface
    """

    def __init__(self, key : str, timeout : int):
        self.api_key = key
        self.timeout = timeout

    def get(self, url: str) -> None:
        """
        The implementation of the abstract method.

        It's painstaking to check inputs, but can save a lot of pain
        down the road by simply checking types match expected types,
        empty values, etc.  
        """
        if not isinstance(url, str):
            raise Exception("Invalid URI")

        print("HttpClient::get - ", url)


"""
    Our "application" code from here down. 
"""
def use_client(client : IApiClient, url : str) -> None:
    """
    A simplified function that takes an instance of IApiClient and a URL 
    in which to "get". 

    Functions are known via the IApiClient interface. While the class *may*
    expose other functionality the code only cares about the interface endpoints.

    The function will verify that it IS in fact an IApiClient before continuing.
    """
    if not isinstance(client, IApiClient):
        raise Exception("Invalid Inteface object")

    print("IApiClient in use ->", type(client))
    client.get(url)


"""
Finally, we can create an instance of IApiClient and then make use of it.

Very derived example....but keeping it super basic to not confuse with too
many details. 
"""
httpClient = HttpClient("api_key", 1020)
use_client(httpClient, "http://DummyUrl")