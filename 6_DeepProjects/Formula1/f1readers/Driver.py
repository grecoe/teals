'''
    Abstraction over data/drivers.csv

    Functionlity not complete, enough to get driver history.
'''

import os,sys,inspect

driver_data_directory = 'data'
driver_data_file = 'drivers.csv'

if __name__ == '__main__':
    # Fix path so we can import readers/base
    currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    base_directory = os.path.dirname(currentdir)
    sys.path.insert(0,base_directory)
    driver_data_directory = os.path.join(base_directory, driver_data_directory) 

# Now it's OK to import
from readers.base import *

class Driver:
    def __init__(self, data_row):
        for key in DriverDataFile.DRIVER_INDEXES:
            setattr(self, key, data_row[DriverDataFile.DRIVER_INDEXES[key]])

class DriverDataFile(DataFile):
    DRIVER_INDEXES = {
        'driverId' : -1,
        'driverRef' : -1,
        'number' : -1,
        'code' : -1,
        'forename' : -1,
        'surname' : -1,
        'dob' : -1,
        'nationality' : -1
        }

    def __init__(self):
        super().__init__(driver_data_directory, driver_data_file)

        for key in DriverDataFile.DRIVER_INDEXES.keys():
            DriverDataFile.DRIVER_INDEXES[key] = self.get_field_index(key)

    def get_by_driver_id(self,driver_id):
        columns = []
        if driver_id:
            columns.append(column_data('driverId',driver_id))

        return self.find(columns)

    def get_by_name(self,first_name, last_name):
        columns = []
        if first_name:
            columns.append(column_data('forename',first_name))
        if last_name:
            columns.append(column_data('surname',last_name))

        return self.find(columns)

    def find(self, column_data_list):
        return_results = []

        results = super().find(column_data_list)
        for result in results:
            return_results.append(Driver(result))

        return return_results

