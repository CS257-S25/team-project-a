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

    # @patch('ProductionCode.datasource.DataSource.get_freq_meetings_attended')
    # def test_route(self, mock_get_freq_meeting_attended):
    #     """Tests a correct path that should display the methods result"""
    #     mock_get_freq_meeting_attended.return_value = "32.71"
    #     self.app = app.test_client()
    #     response = self.app.get("/meeting/frequency", follow_redirects=True)
    #     self.assertEqual(
    #         b"The average percentage of meetings attended is 32.71%", response.data
    #     )

    def test_bad_route(self):
        """Test a bad path that should display a correct usage hint"""
        self.app = app.test_client()
        response = self.app.get("/0", follow_redirects=True)
        self.assertEqual(
            b"404 Not Found: The requested URL was not found on the server. "
            + b"If you entered the URL manually please check your spelling and try again. "
            + b"Sorry, wrong format, do this instead /meeting/frequency or "
            + b"/meeting/count or arrests/low/high",
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

    @patch('ProductionCode.datasource.psycopg2.connect')
    def test_route(self, mock_connect):
        """Tests a correct path that should display the methods result"""
        self.app = app.test_client()
        mock_connect.return_value = self.mock_conn
		#set what it should return
        self.mock_cursor.fetchall.return_value = (
            [[1.6357466063348416]]
            )
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
            + b"/meeting/count or arrests/low/high",
            response.data,
        )


# class TestGetMeetingPage(unittest.TestCase):
#     """Tests the HTML meeting page"""

#     def test_route(self):
#         """Tests a correct path that should display the methods result"""
#         self.app = app.test_client()
#         response = self.app.get("/meeting", follow_redirects=True)
#         print(response.data)
#         self.assertEqual(
#             b"<html>\n\t<head>\n\t\t<title>Self Help Meeting " +
#             b"Attendance\n\t</title>\n\t</head>\n\t<body>\n\t\t<h1>" +
#             b"Self Help Meeting Attendance</h1>\n\t\t" +
#             b"<ul>\n\t\t\t<li>Average meetings attended by " +
#             b"study participants: {{count}}</li>\n\t\t\t<li>" +
#             b"Average frequency of meeting attendance " +
#             b"by study participants: {{freq}}%</li>\n\t\t</ul>\n\t</body>\n</html>",
#             response.data
#         )

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
        response = self.app.get('/arrests/1/10', follow_redirects=True)
        self.assertEqual(b"The number of people who were arrested between 1 and 10 times is: 283",
                          response.data)

    def test_bad_route(self):
        """Test a bad path that should display a correct usage hint"""
        self.app = app.test_client()
        response = self.app.get("/0", follow_redirects=True)
        self.assertEqual(
            b"404 Not Found: The requested URL was not found on the server. " +
            b"If you entered the URL manually please check your spelling and try again. " +
            b"Sorry, wrong format, do this instead /meeting/frequency or " +
            b"/meeting/count or arrests/low/high",
            response.data,
        )
