"""
    General exceptions that must be caught
"""
class DatasetMissingException(Exception):
    def __init__(self, message):
        self.message = message
