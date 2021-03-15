import typing

from ..interfaces import IDataStore
from ..exceptions import InvalidParameterException

class SqlDbDataStore(IDataStore):

    def __init__(self, server : str, user : str, cred : str):
        if not server:
            raise InvalidParameterException("server is empty")
        if not user:
            raise InvalidParameterException("user is empty")
        if not cred:
            raise InvalidParameterException("cred is empty")

    def search(self, search: str) -> typing.Dict[str,str]:
        if not search:
            raise InvalidParameterException("search is empty")

        return {"SqlDbDataStore" : search}
