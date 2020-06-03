'''
    Abstraction over data/status.csv

    Functionlity not complete, enough to get driver history.
'''
from multi_command_utils.data_finder import find_file_root
from multi_command_utils.data_file import DataFile, column_data

status_data_file = 'status.csv'
status_data_directory = find_file_root(status_data_file)


class Status:
    def __init__(self, data_row):
        for key in StatusDataFile.STATUS_INDEXES:
            setattr(self, key, data_row[StatusDataFile.STATUS_INDEXES[key]])

class StatusDataFile(DataFile):
    STATUS_INDEXES = {
        'statusId' : -1,
        'status' : -1
        }

    def __init__(self):
        super().__init__(status_data_directory, status_data_file)

        for key in StatusDataFile.STATUS_INDEXES.keys():
            StatusDataFile.STATUS_INDEXES[key] = self.get_field_index(key)

    def get_by_status_id(self,driver_id):
        columns = []
        if driver_id:
            columns.append(column_data('statusId',driver_id))

        return self.find(columns)

    def find(self, column_data_list):
        return_results = []

        results = super().find(column_data_list)
        for result in results:
            return_results.append(Status(result))

        return return_results

'''
sf = StatusDataFile()
res = sf.find_by_status_id('1')
print(res[0].status)
'''