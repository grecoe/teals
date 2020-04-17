'''
    data_finder :
    
    Utility to find the Formula One data in ANY sub directory of the 
    6_DeepProjects folder. 
'''
import os
import inspect


def find_file_root(file_name):
    currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    base_directory = os.path.dirname(currentdir)
    
    return_path = None
    for root, dirs, files in os.walk(base_directory, topdown=False):
        if file_name in files:
            return_path = root
            break
    return return_path

