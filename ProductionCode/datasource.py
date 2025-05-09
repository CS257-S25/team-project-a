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
        """Gets the average self help meetings attended from the dataset"""

        #Open a cursor to perform database operations
        cursor = self.connection.cursor()

        #Execute a query
        cursor.execute("SELECT avg(cast(NSHLPM as int)) FROM drug_data")

        #Retrieve query results
        records = cursor.fetchall()

        return round(records[0][0], 2)

    def get_freq_meetings_attended(self):
        """Gets the frequency of self help meetings attended from the dataset"""

        #Open a cursor to perform database operations
        cursor = self.connection.cursor()

        cursor.execute("SELECT avg(cast(NSHLPM as int)) FROM drug_data")

        records1 = cursor.fetchall()

        cursor.execute("SELECT max(cast(NSHLPM as int)) FROM drug_data")

        records2 = cursor.fetchall()

        print(records1)

        print(records2)
        return round((records1[0][0]/records2[0][0])*100, 2)

    def get_arrest_ranges(self, low, high):
        """Gets the number of people with in the range 
        of drug sale arrests proivided from the dataset"""

        #Open a cursor to perform database operations
        cursor = self.connection.cursor()

        cursor.execute("SELECT * FROM drug_data WHERE ARSTDRG>=%s" \
        " AND ARSTDRG<=%s ORDER BY ARSTDRG DESC", (low, high,))

        records = cursor.fetchall()


        return len(records)
