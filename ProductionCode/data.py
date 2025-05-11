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

    # def make_data_array(self):
    #     """genrates a 2d array out of the data in the data 0001 file"""
    #     for line in fileinput.input(("Data/ICPSR_30842/DS0001/30842-0001-Data.tsv")):
    #         self.data.append(line.split("\t"))

    # def initialize_data(self):
    #     """ensures that the data is gathered if it is not already"""
    #     if not self.data_initialized:
    #         self.make_data_array()
    #         self.data_initialized = True

    def initalize_dummy_data(self, dummy_data):
        """Allows for dummy data use for testing"""
        self.data = dummy_data
        self.data_initialized = True
