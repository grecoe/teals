'''
    Abstraction over data/races.csv

    Functionlity not complete, enough to get driver history.
'''
from multi_command_utils.data_finder import find_file_root
from multi_command_utils.data_file import DataFile, column_data

races_data_file = 'races.csv'
races_data_directory = find_file_root(races_data_file)

class Race:
    def __init__(self, data_row):
        for key in RacesDataFile.RACES_INDEXES:
            setattr(self, key, data_row[RacesDataFile.RACES_INDEXES[key]])

class RacesDataFile(DataFile):
    RACES_INDEXES = {
        'raceId' : -1,
        'year' : -1,
        'round' : -1,
        'circuitId' : -1,
        'name' : -1,
        'date' : -1
        }

    def __init__(self):
        super().__init__(races_data_directory, races_data_file)

        for key in RacesDataFile.RACES_INDEXES.keys():
            RacesDataFile.RACES_INDEXES[key] = self.get_field_index(key)

    def get_by_race_id(self,race_id):
        columns = []
        if race_id:
            columns.append(column_data('raceId',race_id))

        return self.find(columns)

    def get_by_race_year(self,year):
        columns = []
        if year:
            columns.append(column_data('year',year))

        return self.find(columns)

    def find(self, column_data_list):
        return_results = []

        results = super().find(column_data_list)
        for result in results:
            return_results.append(Race(result))

        return return_results

'''
df = RacesDataFile()
print(df.get_headers())
'''
