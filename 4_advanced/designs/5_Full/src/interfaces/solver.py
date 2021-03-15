"""
    Simple data store interface
"""
import typing
from abc import ABC, abstractmethod
from .datastore import IDataStore

class ISolver(ABC):

    @abstractmethod
    def run(self, dataset: IDataStore) -> typing.Dict[str,object]:
        """
        Solves some random thing using a datastore input.

        Parameters:
        dataset : IDataStore instance

        Returns:
        None

        Throws:
        exceptions.datasetmissing.DatasetMissingException if dataset is invalid type.
        """
        pass
