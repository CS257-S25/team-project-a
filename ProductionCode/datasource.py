"""Runs SQL commands through psql on the database"""

import sys
import psycopg2
from ProductionCode import psql_config as config

class DataSource:
    """Sets up a database that can run sql commands"""

    def __init__(self):
        """Constructor that initiates connection to database"""
        self.connection = self.connect()

    def connect(self):
        """Initiates connection to database using information 
        in the psqlConfig.py file. Returns the connection object."""

        try:
            connection = psycopg2.connect(database=config.DATABASE,
                                          user=config.USER, password=config.PASSWORD,
                                          host="localhost")
        except ConnectionError as e:
            print("Connection error: ", e)
            sys.exit()
        return connection

    def get_ave_meetings_attended(self):
        """Gets the average self help meetings attended from the dataset
        returns a floating point number rounded to two places"""

        #Open a cursor to perform database operations
        cursor = self.connection.cursor()

        #Execute a query
        cursor.execute("SELECT avg(cast(MeetingAttendanceCount as int)) FROM drug_data")

        #Retrieve query results
        records = cursor.fetchall()

        return round(records[0][0], 2)

    def get_freq_meetings_attended(self):
        """Gets the frequency of self help meetings attended from the dataset
        returns a floating point number rounded to 2 places"""

        #Open a cursor to perform database operations
        cursor = self.connection.cursor()

        cursor.execute("SELECT avg(cast(MeetingAttendanceCount as int)) FROM drug_data")
        records1 = cursor.fetchall()

        cursor.execute("SELECT max(cast(MeetingAttendanceCount as int)) FROM drug_data")
        records2 = cursor.fetchall()

        return round((records1[0][0]/records2[0][0])*100, 2)

    def get_arrest_ranges(self, low, high):
        """Gets the number of people with in the range 
        of drug sale arrests proivided from the dataset
        takes in two integers for the range of arrests, returns an integer"""

        #Open a cursor to perform database operations
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM drug_data WHERE DrugRelatedArrests>=%s" \
        " AND DrugRelatedArrests<=%s ORDER BY DrugRelatedArrests DESC", (low, high,))

        records = cursor.fetchall()
        return len(records)

    def get_alcohol_phyisical_health(self):
        """Gets the frequency at which patients' physical
        health is affected by alcohol"""

        cursor = self.connection.cursor()
        cursor.execute("SELECT max(cast(AlcoholUsePhysicalHealth as int)) FROM drug_data")

        records = cursor.fetchall()
        return round(records[0][0], 2)

    def get_alcohol_mental_health(self):
        """Gets the frequency at which patients' mental
        health is affected by alcohol"""

        cursor = self.connection.cursor()
        cursor.execute("SELECT max(cast(AlcoholUseEmotionalHealth as int)) FROM drug_data")

        records = cursor.fetchall()
        return round(records[0][0], 2)

    def get_drug_physical_health(self):
        """Gets the frequency at which patients' physical
        health is affected by drugs"""

        cursor = self.connection.cursor()
        cursor.execute("SELECT max(cast(DrugUsePhysicalHealth as int)) FROM drug_data")

        records = cursor.fetchall()
        return round(records[0][0], 2)

    def get_drug_mental_health(self):
        """Gets the frequency at which patients' mental
        health is affected by drugs"""

        cursor = self.connection.cursor()
        cursor.execute("SELECT max(cast(DrugUseEmotionalHealth as int)) FROM drug_data")

        records = cursor.fetchall()
        return round(records[0][0], 2)

    def get_graph_data(self):
        """Gets the data needed for a graph relating drug affect 
        on emotional state and self help meetings attended,
        returns a array of points"""

        #Open a cursor to perform database operations
        cursor = self.connection.cursor()

        cursor.execute("SELECT cast(MeetingAttendanceCount as int) FROM drug_data")

        records1 = cursor.fetchall()

        cursor.execute("SELECT DrugUseEmotionalHealth FROM drug_data")

        records2 = cursor.fetchall()
        return process_graph_data(records1, records2)

def process_graph_data(list1, list2):
    """Gets the data into ann x, y list from the sql returned info,
    returns an array of points from the two arrays"""
    result = []
    for i, item in enumerate(list1):
        if item[0] != -9 and item[0] is not None and list2[i][0] is not None:
            result.append([item[0], list2[i][0]])
    return result
