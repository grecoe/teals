'''
    Using multi_command_utils/data_file.py

    The data used for this example comes from a talk I did on Machine Learning. 
    While that topic is irrelevant, it was a useful and sufficiently large 
    data set to show off how to use the DataFile class.
   
    Given the folder structure, we first must set the path to the root path
    (6_DeepProjects) so that the script will be able to find and load our 
    utilities.
'''

import os
import sys
import inspect

core_directory = '6_DeepProjects'
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))

dir_split = os.path.split(currentdir)
while dir_split[1] != core_directory:
    currentdir = dir_split[0]
    dir_split = os.path.split(currentdir)
# Now that we have the core directory, we can now start importing 
# what we need once we set the path. 
sys.path.insert(0,currentdir)

'''
    Now we can import the application and it will load ok. 
'''
from multi_command_utils.data_file import DataFile, column_data

# Create the class instance, remeber we had to change the dir above to read
# the utilities directory.
my_data_file = DataFile(os.path.join(currentdir,"FileData"), "dataset.csv")

# Now print out the headers
print("HEADERS:", my_data_file.get_headers())

# Getting column indexes when you get rows back
print("Header indexes")
for hdr in my_data_file.get_headers():
    print(hdr,'=', my_data_file.get_field_index(hdr))

# How many unique id's are there? 
id_col = my_data_file.get_column_by_name('id')
unique_ids = set(id_col)
print("There are {} unique device ID's in the data".format(len(unique_ids)))

# Get only the records for device 1, to do that we create a column
# collection to use for the query. 
dev_1_column_data = column_data('id', '1')
dev_1_data = my_data_file.find([dev_1_column_data])
print("Found {} entries for device 1 ".format(len(dev_1_data)))

# Expand the search more. Find a record for 
#   id = 6 and time = 284
dev_6_id_col = column_data('id', '6')
dev_6_time_col = column_data('time', '284')
dev_6_entry = my_data_file.find([dev_6_id_col, dev_6_time_col])
print("Found {} entries for device 6 at time 284".format(len(dev_6_entry)))
for dev_entry in dev_6_entry:
    print(dev_entry)
