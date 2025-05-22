"""Test code for flask app"""

import unittest
from unittest.mock import MagicMock, patch

from app import app


class TestMainPage(unittest.TestCase):
    """Tests the apps home page"""

    def __init__(self, methodName="runTest"):
        super().__init__(methodName)
        self.app = app.test_client()

    def test_route(self):
        """Tests that the home page has the correct welcome text"""
        self.app = app.test_client()
        response = self.app.get("/", follow_redirects=True)
        self.assertIn(
            b'<p>This is a site designed to ' +
            b'facilitate the analysis of a \n        ' +
            b'survey on people who have suffered from drug abuse and as a ' +
            b'result have been arrested.</p>',
            response.data,
        )


class TestGetMeetingFrequency(unittest.TestCase):
    """Tests the path based method calls and pages"""

    def __init__(self, methodName="runTest"):
        super().__init__(methodName)
        self.app = app.test_client()

    def setUp(self):
        """Sets up the dummy data"""
        self.mock_conn = MagicMock()
        self.mock_cursor = self.mock_conn.cursor.return_value

    # @patch('ProductionCode.datasource.DataSource.get_freq_meetings_attended')
    # def test_route(self, mock_connect):
    #     """Tests a correct path that should display the methods result"""
    #     mock_connect.return_value = self.mock_conn
    # 	#set what it should return
    #     self.mock_cursor.fetchall.return_value = (
    #         [[1]]
    #         )
    #     self.app = app.test_client()
    #     response = self.app.get("/meeting/frequency", follow_redirects=True)
    #     print(response.data)
    #     self.assertEqual(
    #         b"The average percentage of meetings attended is 100%", response.data
    #     )

    def test_bad_route(self):
        """Test a bad path that should display a correct usage hint"""
        self.app = app.test_client()
        response = self.app.get("/0", follow_redirects=True)
        self.assertEqual(
            b"404 Not Found: The requested URL was not found on the server. "
            + b"If you entered the URL manually please check your spelling and try again. "
            + b"Sorry, wrong format, do this instead /meeting/frequency or "
            + b"/meeting/count or arrests/low/high eg. sellArrest/1/3",
            response.data,
        )


class TestGetMeetingCount(unittest.TestCase):
    """Tests the path based method calls and pages"""

    def __init__(self, methodName="runTest"):
        super().__init__(methodName)
        self.app = app.test_client()

    def setUp(self):
        """Sets up the dummy data"""
        self.mock_conn = MagicMock()
        self.mock_cursor = self.mock_conn.cursor.return_value

    @patch("ProductionCode.datasource.psycopg2.connect")
    def test_route(self, mock_connect):
        """Tests a correct path that should display the methods result"""
        self.app = app.test_client()
        mock_connect.return_value = self.mock_conn
        # set what it should return
        self.mock_cursor.fetchall.return_value = [[1.6357466063348416]]
        response = self.app.get("/meeting/count", follow_redirects=True)
        self.assertEqual(
            b"The average number of self-help meetings attended is 1.64", response.data
        )

    def test_bad_route(self):
        """Test a bad path that should display a correct usage hint"""
        self.app = app.test_client()
        response = self.app.get("/0", follow_redirects=True)
        self.assertEqual(
            b"404 Not Found: The requested URL was not found on the server. "
            + b"If you entered the URL manually please check your spelling and try again. "
            + b"Sorry, wrong format, do this instead /meeting/frequency or "
            + b"/meeting/count or arrests/low/high eg. sellArrest/1/3",
            response.data,
        )


class TestGetMeetingPage(unittest.TestCase):
    """Tests the HTML meeting page"""

    def __init__(self, methodName="runTest"):
        super().__init__(methodName)
        self.app = app.test_client()

    def setUp(self):
        """Sets up the dummy data"""
        self.mock_conn = MagicMock()
        self.mock_cursor = self.mock_conn.cursor.return_value

    @patch("ProductionCode.datasource.psycopg2.connect")
    def test_route(self, mock_connect):
        """Tests a correct path that should display the methods result"""
        self.app = app.test_client()
        mock_connect.return_value = self.mock_conn
        # set what it should return
        self.mock_cursor.fetchall.return_value = [[1.6357466063348416]]
        response = self.app.get("/meeting", follow_redirects=True)
        self.assertIn(
            b'li>Average meetings attended by study participants: 1.64</li>' +
            b'\n                <li>Average frequency of meeting attendance by study ' +
            b'participants: 100.0%</li>',
            response.data,
        )

class TestDrugSaleArrests(unittest.TestCase):
    """Tests the drug sale arrests route"""

    def __init__(self, methodName="runTest"):
        super().__init__(methodName)
        self.app = app.test_client()

    def setUp(self):
        """Sets up the dummy data"""
        self.mock_conn = MagicMock()
        self.mock_cursor = self.mock_conn.cursor.return_value

    @patch('ProductionCode.datasource.psycopg2.connect')
    def test_drug_sale(self, mock_connect):
        """Test for route for drug sale arrests"""
        self.app = app.test_client()
        mock_connect.return_value = self.mock_conn
        #set what it should return
        self.mock_cursor.fetchall.return_value = (
            [None]*283
            )
        response = self.app.get('/sellArrest/lower/upper?lower=1&upper=10', follow_redirects=True)
        self.assertIn(b'The number of people who were arrested between 1 and 10<br>' +
                      b'\n        times is: 283',
                          response.data)

def test_bad_route(self):
    """Test a bad path that should display a correct usage hint"""
    self.app = app.test_client()
    response = self.app.get("/0", follow_redirects=True)
    self.assertEqual(
        b"404 Not Found: The requested URL was not found on the server. " +
        b"If you entered the URL manually please check your spelling and try again. " +
        b"Sorry, wrong format, do this instead /meeting/frequency or " +
        b"/meeting/count or arrests/low/high eg. sellArrest/1/3",
        response.data,
    )
