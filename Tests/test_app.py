"""Test code"""

import unittest
from app import app
from ProductionCode import data_processor

dummyData = [
    ["NSHLPM", "ARSTDRG"],
    ["3", "1"],
    ["20", "6"],
    ["4", "15"],
    ["0", "9"],
    [" ", " "],
]


class TestMainPage(unittest.TestCase):
    """Tests the apps home page"""

    def __init__(self, methodName = "runTest"):
        super().__init__(methodName)
        self.app = app.test_client()

    def test_route(self):
        """Tests that the home page has the correct welcome text"""
        self.app = app.test_client()
        response = self.app.get("/", follow_redirects=True)
        self.assertEqual(
            b"Hello, this is the homepage. " +
            b"To find the frequency of meeting attended please do (url)/meeting/[frequency, count]",
            response.data,
        )


class TestGetMeetingFrequency(unittest.TestCase):
    """Tests the path based method calls and pages"""

    def __init__(self, methodName = "runTest"):
        super().__init__(methodName)
        self.app = app.test_client()

    def setUp(self):
        """Sets up the dummy data"""
        data_processor.initalize_dummy_data(dummyData)

    def test_route(self):
        """Tests a correct path that should display the methods result"""
        self.app = app.test_client()
        response = self.app.get("/meeting/frequency", follow_redirects=True)
        self.assertEqual(
            b"The average percentage of meetings attended is 33.75%", response.data
        )

    def test_bad_route(self):
        """Test a bad path that should display a correct usage hint"""
        self.app = app.test_client()
        response = self.app.get("/0", follow_redirects=True)
        self.assertEqual(
            b"404 Not Found: The requested URL was not found on the server. " +
            b"If you entered the URL manually please check your spelling and try again. " +
            b"Sorry, wrong format, do this instead (url)/meeting/[frequency, count]",
            response.data,
        )


class TestGetMeetingCount(unittest.TestCase):
    """Tests the path based method calls and pages"""

    def __init__(self, methodName = "runTest"):
        super().__init__(methodName)
        self.app = app.test_client()

    def setUp(self):
        """Sets up the dummy data"""
        data_processor.initalize_dummy_data(dummyData)

    def test_route(self):
        """Tests a correct path that should display the methods result"""
        self.app = app.test_client()
        response = self.app.get("/meeting/count", follow_redirects=True)
        self.assertEqual(
            b"The average number of meetings attended is 6.75", response.data
        )

    def test_bad_route(self):
        """Test a bad path that should display a correct usage hint"""
        self.app = app.test_client()
        response = self.app.get("/0", follow_redirects=True)
        self.assertEqual(
            b"404 Not Found: The requested URL was not found on the server. " +
            b"If you entered the URL manually please check your spelling and try again. " +
            b"Sorry, wrong format, do this instead (url)/meeting/[frequency, count]",
            response.data,
        )