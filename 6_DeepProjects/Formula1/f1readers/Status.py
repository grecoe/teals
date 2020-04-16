'''
    Abstraction over data/status.csv

    Functionlity not complete, enough to get driver history.
'''

import os,sys,inspect

status_data_directory = 'data'
status_data_file = 'status.csv'

if __name__ == '__main__':
    # Fix path so we can import readers/base
    currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    base_directory = os.path.dirname(currentdir)
    sys.path.insert(0,base_directory)
    status_data_directory = os.path.join(base_directory, status_data_directory) 

# Now it's OK to import
from readers.base import *

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