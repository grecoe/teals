'''
    Abstraction over data/drivers.csv

    Functionlity not complete, enough to get driver history.
'''
from multi_command_utils.data_finder import find_file_root
from multi_command_utils.data_file import DataFile, column_data

driver_data_file = 'drivers.csv'
driver_data_directory = find_file_root(driver_data_file)

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

