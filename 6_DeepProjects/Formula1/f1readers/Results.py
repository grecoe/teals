'''
    Abstraction over data/results.csv

    Functionlity not complete, enough to get driver history.
'''
import os,sys,inspect

results_data_directory = 'data'
results_data_file = 'results.csv'

if __name__ == '__main__':
    # Fix path so we can import readers/base
    currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    base_directory = os.path.dirname(currentdir)
    sys.path.insert(0,base_directory)
    results_data_directory = os.path.join(base_directory, results_data_directory) 

# Now it's OK to import
from readers.base import *


class Result:
    def __init__(self, data_row):
        for key in ResultsDataFile.RESULTS_INDEXES:
            setattr(self, key, data_row[ResultsDataFile.RESULTS_INDEXES[key]])

    def is_front_row_start(self):
        grid = self.grid.strip()
        return grid and grid  in ['1','2']
    
    def is_pole_position(self):
        grid = self.grid.strip()
        return grid and grid in ['1']
    
    def is_podium(self):
        position = self.position.strip()
        return position and position in ['1','2','3'] 

    def is_dnf(self):
        return not self.position.strip() 

class ResultsDataFile(DataFile):
    RESULTS_INDEXES = {
        'resultId' : -1,
        'raceId' : -1,
        'driverId' : -1,
        'constructorId' : -1,
        'number' : -1,
        'grid' : -1,
        'position' : -1,
        'positionText' : -1,
        'positionOrder' : -1,
        'points' : -1,
        'laps' : -1,
        'time' : -1,
        'milliseconds' : -1,
        'fastestLap' : -1,
        'rank' : -1,
        'fastestLapTime' : -1,
        'fastestLapSpeed' : -1,
        'statusId' : -1
        }

    def __init__(self):
        super().__init__(results_data_directory, results_data_file)

        for key in ResultsDataFile.RESULTS_INDEXES.keys():
            ResultsDataFile.RESULTS_INDEXES[key] = self.get_field_index(key)

    def get_by_driver_id(self,driver_id):
        columns = []
        if driver_id:
            columns.append(column_data('driverId',driver_id))

        return self.find(columns)

    def get_by_race_id(self,race_id):
        columns = []
        if race_id:
            columns.append(column_data('raceId',race_id))

        return self.find(columns)

    def find(self, column_data_list):
        return_results = []

        results = super().find(column_data_list)
        for result in results:
            return_results.append(Result(result))

        return return_results

'''
df = ResultsDataFile()
print(df.get_headers())
quit()
'''