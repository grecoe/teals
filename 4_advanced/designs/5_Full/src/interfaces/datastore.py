"""
    Simple data store interface
"""
import typing
from abc import ABC, abstractmethod

class IDataStore(ABC):

    @abstractmethod
    def search(self, search: str) -> typing.Dict[str,str]:
        """
        Internally loads a dataset by 'name'. 

        Parameters:
        search : query to perform on dataset

        Returns:
        Dictionary of str/str containing key values 

        Throws:
        exceptions.datasetmissing.InvalidParameterException if search is empty.
        exceptions.datasetmissing.DatasetMissingException if dataset is not loaded.
        """
        pass
