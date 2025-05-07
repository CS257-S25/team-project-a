"""Test code for flask app"""

import unittest
from unittest.mock import MagicMock, patch
from test_cl import dummyData
from app import app, drug_sale, get_meeting_count, get_meeting_freq
from ProductionCode import data_processor


class TestMainPage(unittest.TestCase):
    """Tests the apps home page"""

    def __init__(self, methodName="runTest"):
        super().__init__(methodName)
        self.app = app.test_client()

    def test_route(self):
        """Tests that the home page has the correct welcome text"""

        self.app = app.test_client()
        response = self.app.get("/", follow_redirects=True)
        self.assertEqual(
            b"Hello! Welcome to our website with the amazingly"
            b"curated title: Analyzing Criminal Drug Abuse Treatment in Females"
            b"\nAlso known as drug_abuse_treatment.py"
            b"\n"
            b"\n"
            b"Here are the main directories of our program for your research/interests: "
            b"\nFor frequencies or counts of meeting attendance: (url)/meeting/[frequency], [count]"
            b"\nFor drug sale arrests amount: "
            b"(url)/drug-sale-arrests/lowerBoundCount/upperBoundCount",
            response.data,
        )


class TestGetMeetingFrequency(unittest.TestCase):
    """Tests the path based method calls and pages"""

    def __init__(self, methodName="runTest"):
        super().__init__(methodName)
        self.app = app.test_client()
    
    def setUp(self):
        #create a mock connection and cursor
        self.mock_conn = MagicMock()
        self.mock_cursor = self.mock_conn.cursor.return_value

    @patch('ProductionCode.datasource.psycopg2.connect')
    def test_route(self, mock_connect):
        """Tests a correct path that should display the methods result"""
        mock_connect.return_value = self.mock_conn
		#set what it should return
        self.mock_cursor.fetchone.return_value(
            "The average percentage of meetings attended is 32.71%"
            )
        self.assertEqual(get_meeting_freq(),
            "The average percentage of meetings attended is 32.71%"
            )


class TestGetMeetingCount(unittest.TestCase):
    """Tests the path based method calls and pages"""

    def __init__(self, methodName="runTest"):
        super().__init__(methodName)
        self.app = app.test_client()

    def setUp(self):
        #create a mock connection and cursor
        self.mock_conn = MagicMock()
        self.mock_cursor = self.mock_conn.cursor.return_value

    @patch('ProductionCode.datasource.psycopg2.connect')
    def test_route(self, mock_connect):
        """Tests a correct path that should display the methods result"""
        mock_connect.return_value = self.mock_conn
		#set what it should return
        self.mock_cursor.fetchone.return_value(
            "The average number of meetings attended is 1.64"
            )
        self.assertEqual(
            get_meeting_count(),
            "The average number of meetings attended is 1.64"
        )



class TestDrugSaleArrests(unittest.TestCase):
    """Tests the drug sale arrests route"""

    def __init__(self, methodName="runTest"):
        super().__init__(methodName)
        self.app = app.test_client()

    def setUp(self):
        #create a mock connection and cursor
        self.mock_conn = MagicMock()
        self.mock_cursor = self.mock_conn.cursor.return_value

    @patch('ProductionCode.datasource.psycopg2.connect')
    def test_drug_sale(self, mock_connect):
        """Test for route for drug sale arrests"""
        mock_connect.return_value = self.mock_conn
		#set what it should return
        self.mock_cursor.fetchone.return_value("283 people")
        self.assertEqual(drug_sale(1, 10), "283 people")
