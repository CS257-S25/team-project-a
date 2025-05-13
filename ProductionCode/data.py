"""Manages the data in an array"""

import fileinput


class Data:
    """Holds the data informaton"""

    def __init__(self):
        self.data = []
        """Initiaizes the data"""
        for line in fileinput.input(("Data/ICPSR_30842/DS0001/30842-0001-Data.tsv")):
            self.data.append(line.split("\t"))
        self.data_initialized = True

    def is_data_initialized(self):
        """Checks if the data object is initialized"""
        return self.data_initialized

    def initalize_dummy_data(self, dummy_data):
        """Allows for dummy data use for testing"""
        self.data = dummy_data
        self.data_initialized = True
