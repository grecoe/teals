import typing
from ..interfaces import ISolver, IDataStore
from ..exceptions import DatasetMissingException, InvalidParameterException

class DummySolver(ISolver):

    def __init__(self, data_store : IDataStore, store_query : str):
        if not isinstance(data_store, IDataStore):
            raise InvalidParameterException("Data store is not an IDataStore")
        if not store_query:
            raise InvalidParameterException("store_query is empty")
        
        self.datastore = data_store
        self.store_query = store_query

    def run(self) -> typing.Dict[str,object]:

        if not self.datastore:
            raise DatasetMissingException("self.datastore")

        return_dict = {}
        return_dict.update(self.datastore.search(self.store_query))            

        return return_dict