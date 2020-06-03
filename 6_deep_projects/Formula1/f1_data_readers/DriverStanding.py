'''
    Abstraction over data/drivers.csv

    Functionlity not complete, enough to get driver history.
'''
from multi_command_utils.data_finder import find_file_root
from multi_command_utils.data_file import DataFile, column_data

driver_standing_data_file = 'driverStandings.csv'
driver_standing_data_directory = find_file_root(driver_standing_data_file)

class DriverStanding:
    def __init__(self, data_row):
        for key in DriverStandingFile.DRIVER_STANDING_INDEXES:
            setattr(self, key, data_row[DriverStandingFile.DRIVER_STANDING_INDEXES[key]])

class DriverStandingFile(DataFile):
    DRIVER_STANDING_INDEXES = {
        'driverStandingsId' : -1,
        'raceId' : -1,
        'driverId' : -1,
        'points' : -1,
        'position' : -1,
        'positionText' : -1,
        'wins' : -1
        }

    def __init__(self):
        super().__init__(driver_standing_data_directory, driver_standing_data_file)

        for key in DriverStandingFile.DRIVER_STANDING_INDEXES.keys():
            DriverStandingFile.DRIVER_STANDING_INDEXES[key] = self.get_field_index(key)

    def get_by_driver_id(self,driver_id):
        columns = []
        if driver_id:
            columns.append(column_data('driverId',driver_id))

        return self.find(columns)

    def find(self, column_data_list):
        return_results = []

        results = super().find(column_data_list)
        for result in results:
            return_results.append(DriverStanding(result))

        return return_results

