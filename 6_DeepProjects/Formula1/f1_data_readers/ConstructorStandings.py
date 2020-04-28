'''
    Abstraction over data/constructorStandings.csv

    Functionlity not complete, enough to get driver history.
'''
from multi_command_utils.data_finder import find_file_root
from multi_command_utils.data_file import DataFile, column_data

constructor_data_file = 'constructorStandings.csv'
constructor_data_directory = find_file_root(constructor_data_file)

class ConstructorStanding:
    def __init__(self, data_row):
        for key in ConstructorStandingsDataFile.CONSTRUCTOR_INDEXES:
            setattr(self, key, data_row[ConstructorStandingsDataFile.CONSTRUCTOR_INDEXES[key]])

class ConstructorStandingsDataFile(DataFile):
    CONSTRUCTOR_INDEXES = {
        "constructorStandingsId" : -1 ,
        'raceId' : -1,
        'constructorId' : -1,
        'points' : -1,
        'position' : -1,
        'positionText' : -1,
        'wins' : -1
        }

    def __init__(self):
        super().__init__(constructor_data_directory, constructor_data_file)

        for key in ConstructorStandingsDataFile.CONSTRUCTOR_INDEXES.keys():
            ConstructorStandingsDataFile.CONSTRUCTOR_INDEXES[key] = self.get_field_index(key)

    def get_by_race_id(self,id):
        columns = []
        if id:
            columns.append(column_data('raceId',id))

        return self.find(columns)

    def get_by_constructor_id(self,id):
        columns = []
        if id:
            columns.append(column_data('constructorId',id))

        return self.find(columns)

    def find(self, column_data_list):
        return_results = []

        results = super().find(column_data_list)
        for result in results:
            return_results.append(ConstructorStanding(result))

        return return_results
