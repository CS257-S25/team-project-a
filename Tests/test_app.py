"""Test code for flask app"""

import unittest
from test_cl import dummyData
from app import app
from ProductionCode import data_processor
<<<<<<< HEAD

=======
>>>>>>> dc203e19002f144c74083e96d09654573bf76e08


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
        """Sets up the dummy data"""
        data_processor.data_obj.initalize_dummy_data(dummyData)

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
            b"404 Not Found: The requested URL was not found on the server. "
            + b"If you entered the URL manually please check your spelling and try again. "
            + b"Sorry, wrong format, do this instead "
            + b"(url)/meeting/[frequency, count] or "
            + b"(url)/drug-sale-arrests/lowerBoundCount/upperBoundCount",
            response.data,
        )


class TestGetMeetingCount(unittest.TestCase):
    """Tests the path based method calls and pages"""

    def __init__(self, methodName="runTest"):
        super().__init__(methodName)
        self.app = app.test_client()

    def setUp(self):
        """Sets up the dummy data"""
        data_processor.data_obj.initalize_dummy_data(dummyData)

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
            b"404 Not Found: The requested URL was not found on the server. "
            + b"If you entered the URL manually please check your spelling and try again. "
            + b"Sorry, wrong format, do this instead "
            + b"(url)/meeting/[frequency, count] or "
            + b"(url)/drug-sale-arrests/lowerBoundCount/upperBoundCount",
            response.data,
        )


class TestDrugSaleArrests(unittest.TestCase):
    """Tests the drug sale arrests route"""

    def __init__(self, methodName="runTest"):
        super().__init__(methodName)
        self.app = app.test_client()

    def setUp(self):
        """Sets up the dummy data"""
        data_processor.data_obj.initalize_dummy_data(dummyData)

    def test_drug_sale(self):
        """Test for route for drug sale arrests"""
        response = self.app.get('/drug-sale-arrests/1/10', follow_redirects=True)
        self.assertEqual(b"283 people", response.data)

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
