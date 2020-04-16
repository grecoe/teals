'''
    Abstraction over data/races.csv

    Functionlity not complete, enough to get driver history.
'''
import os,sys,inspect

races_data_directory = 'data'
races_data_file = 'races.csv'

if __name__ == '__main__':
    # Fix path so we can import readers/base
    currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    base_directory = os.path.dirname(currentdir)
    sys.path.insert(0,base_directory)
    races_data_directory = os.path.join(base_directory, races_data_directory) 

# Now it's OK to import
from readers.base import *

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
