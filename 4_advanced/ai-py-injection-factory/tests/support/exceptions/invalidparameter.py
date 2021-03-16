"""
    General exceptions that must be caught
"""
class InvalidParameterException(Exception):
    def __init__(self, message):
        self.message = message