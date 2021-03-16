import typing
from ..interfaces import IDataStore
from ..exceptions import InvalidParameterException

class AzureStorageDataStore(IDataStore):

    def __init__(self, connection_string : str):
        if not connection_string:
            raise InvalidParameterException("connection_string is empty")

        self.connection_string = connection_string


    def search(self, search: str) -> typing.Dict[str,str]:
        if not search:
            raise InvalidParameterException("search is empty")

        return {"AzureStorageDataStore" : search}
