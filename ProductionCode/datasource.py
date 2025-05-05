"""Runs SQL commands through psql on the database"""

import sys
import psycopg2
import psqlConfig as config

class DataSource:
    """Sets up a database that can run sql commands"""

    def __init__(self):
        '''Constructor that initiates connection to database'''
        self.connection = self.connect()

    def connect(self):
        '''Initiates connection to database using information in the psqlConfig.py file.
        Returns the connection object.'''

        try:
            connection = psycopg2.connect(database=config.database,
                                          user=config.user, password=config.password,
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

        print(records)
