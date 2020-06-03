'''
    Abstraction over data/constructors.csv

    Functionlity not complete, enough to get driver history.
'''
from multi_command_utils.data_finder import find_file_root
from multi_command_utils.data_file import DataFile, column_data

constructor_data_file = 'constructors.csv'
constructor_data_directory = find_file_root(constructor_data_file)

class Constructor:
    def __init__(self, data_row):
        for key in ConstructorsDataFile.CONSTRUCTOR_INDEXES:
            setattr(self, key, data_row[ConstructorsDataFile.CONSTRUCTOR_INDEXES[key]])

class ConstructorsDataFile(DataFile):
    CONSTRUCTOR_INDEXES = {
        "constructorId" : -1 ,
        'constructorRef' : -1,
        'name' : -1,
        'nationality' : -1
        }

    def __init__(self):
        super().__init__(constructor_data_directory, constructor_data_file)

        for key in ConstructorsDataFile.CONSTRUCTOR_INDEXES.keys():
            ConstructorsDataFile.CONSTRUCTOR_INDEXES[key] = self.get_field_index(key)

    def get_by_id(self,id):
        columns = []
        if id:
            columns.append(column_data('constructorId',id))

        return self.find(columns)

    def find(self, column_data_list):
        return_results = []

        results = super().find(column_data_list)
        for result in results:
            return_results.append(Constructor(result))

        return return_results
