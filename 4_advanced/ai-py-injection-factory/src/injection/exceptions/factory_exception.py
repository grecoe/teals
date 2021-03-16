"""
(c) Microsoft. All rights reserved.
"""


class FactoryException(Exception):
    """
    Base exception for factory
    """
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message