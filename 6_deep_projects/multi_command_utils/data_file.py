'''
    Base file reader for any CSV file. 
'''
import csv
import os
import collections

column_data = collections.namedtuple("column", "id value")


class DataFile:
    '''
        This is a base class for all other data file classes. 

        All data files created are CSV, so this makes a perfect
        opportunity to use class derivation to have a base class
        perform the generic functionaity. 
    '''
    def __init__(self, directory, file_name):
        self.directory = directory
        self.file_name = file_name
        self.header = None
        self.data = []
        self._load_data()

    def get_headers(self):
        return self.header

    def get_field_index(self, column_name):
        if column_name not in self.header:
            raise Exception("Column {} not in dataset".format(column_name))

        return self.header.index(column_name)

    def get_column_by_name(self, column_name):
        hdr_index = self.get_field_index(column_name)
        return self.get_column_by_index(hdr_index)

    def get_column_by_index(self, column_index):
        if column_index not in range(len(self.header)):
            raise Exception("Invalid header index {}".format(column_index))

        return [row_data[column_index] for row_data in self.data]

    def find(self, column_data_list):
        '''
            Find records in the data set

            column_data_list :  This is a list of column_data (named_tuples)
                                that identify columns to search and values to 
                                match (case insensitive). 

                                If no list is provided the full data set (rows)
                                are returned. 
        '''
        return_data = []
        if not column_data_list:
            return_data = self.data
        else:
            search_data = []
            for data in column_data_list:
                search_data.append( (self.header.index(data.id), data.value) )
        
            for hdr_index in search_data:
                if len(return_data) == 0:
                    return_data = self.data

                return_data = [
                    row_data 
                    for 
                    row_data in return_data 
                    if str(row_data[hdr_index[0]]).lower() == str(hdr_index[1]).lower()
                    ]

        return return_data 

    def _load_data(self):
        file_path = os.path.join(self.directory, self.file_name)
        line = 1
        with open(file_path,'r', encoding='ASCII', errors="surrogateescape") as input_file:
            rows = input_file.readlines()
            #csvReader = csv.reader(input_file)
            try:
                for row in rows:
                    row = row.strip(' \n')
                    row_data = row.split(',')
                    if not self.header:
                        self.header = row_data
                    else:
                        self.data.append(row_data)
                    line += 1
            except Exception as ex:
                print("ERROR LINE", line)
                raise ex