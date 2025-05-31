"""Test code for flask app"""

import unittest
from unittest.mock import MagicMock, patch

from ProductionCode.datasource import DataSource
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
            b'<h2>Info:</h2>',
            response.data,
        )

class TestGetMeetingCount(unittest.TestCase):
    """Tests the path based method calls and pages"""

    def __init__(self, methodName="runTest"):
        super().__init__(methodName)
        self.app = app.test_client()

    @patch("ProductionCode.datasource.psycopg2.connect")
    def setUp(self, mock_connect):
        """Sets up the mock database"""
        self.mock_conn = MagicMock()
        self.mock_cursor = self.mock_conn.cursor.return_value
        mock_connect.return_value = self.mock_conn
        self.data_soucre = DataSource()

    def test_route(self):
        """Tests a correct path that should display the methods result"""
        self.data_soucre.connection.cursor().fetchall.return_value = [[1.6357466063348416]]
        response = self.app.get("/meeting/count", follow_redirects=True)
        self.assertEqual(
            b"The average number of self-help meetings attended is 1.64", response.data
        )

class TestGetMeetingPage(unittest.TestCase):
    """Tests the HTML meeting page"""

    def __init__(self, methodName="runTest"):
        super().__init__(methodName)
        self.app = app.test_client()

    @patch("ProductionCode.datasource.psycopg2.connect")
    def setUp(self, mock_connect):
        """Sets up the mock database"""
        self.mock_conn = MagicMock()
        self.mock_cursor = self.mock_conn.cursor.return_value
        mock_connect.return_value = self.mock_conn
        self.data_soucre = DataSource()

    def test_route(self):
        """Tests a correct path that should display the methods result"""
        self.data_soucre.connection.cursor().fetchall.return_value = [[1.6357466063348416]]
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

    @patch('ProductionCode.datasource.psycopg2.connect')
    def setUp(self, mock_connect):
        """Sets up the mock database"""
        self.mock_conn = MagicMock()
        self.mock_cursor = self.mock_conn.cursor.return_value
        mock_connect.return_value = self.mock_conn
        self.data_soucre = DataSource()

    def test_drug_sale_main_page(self):
        """Tests that the home page has the correct welcome text"""
        response = self.app.get("/sellArrest", follow_redirects=True)
        self.assertIn(
            b'Please enter your lower and upper bounds as directed',
            response.data,
        )

    def test_drug_sale_result_page(self):
        """Test for route for drug sale arrests"""
        self.data_soucre.connection.cursor().fetchall.return_value = (
            [None]*283
            )
        response = self.app.get('/sellArrest/lower/upper?lower=1&upper=10', follow_redirects=True)
        self.assertIn(b'The number of people who were arrested between 1 and 10<br>' +
                      b'\n        times is: 283',
                          response.data)

class TestDataOverview(unittest.TestCase):
    """Tests the HTML data overview page"""

    def __init__(self, methodName="runTest"):
        super().__init__(methodName)
        self.app = app.test_client()

    @patch('ProductionCode.datasource.psycopg2.connect')
    def setUp(self, mock_connect):
        """Sets up the mock database"""
        self.mock_conn = MagicMock()
        self.mock_cursor = self.mock_conn.cursor.return_value
        mock_connect.return_value = self.mock_conn
        self.data_soucre = DataSource()

    def test_route(self):
        """Tests a correct path that should display the data overview page"""
        response = self.app.get("/dataOverview", follow_redirects=True)
        self.data_soucre.connection.cursor().fetchall.return_value = (
            [[1, 1],[1, 1]]
            )
        self.assertIn(
            b'<h2 id="exclusive">Data Overview</h2>',
            response.data,
        )

class Test404Page(unittest.TestCase):
    """Tests the HTML data overview page"""

    def __init__(self, methodName="runTest"):
        super().__init__(methodName)
        self.app = app.test_client()

    def setUp(self):
        """Sets up the mock database"""
        self.mock_conn = MagicMock()
        self.mock_cursor = self.mock_conn.cursor.return_value

    @patch('ProductionCode.datasource.psycopg2.connect')
    def test_bad_route(self, mock_connect):
        """Tests a bad path that should display the 404 page"""
        mock_connect.return_value = self.mock_conn
        response = self.app.get("/ahidhd", follow_redirects=True)
        self.assertIn(
            b'<h2>Error 404:</h2>',
            response.data,
        )


class TestSearch(unittest.TestCase):
    """Tests the search page"""

    def __init__(self, methodName="runTest"):
        super().__init__(methodName)
        self.app = app.test_client()

    @patch("ProductionCode.datasource.psycopg2.connect")
    def setUp(self, mock_connect):
        """Sets up the mock database"""
        self.mock_conn = MagicMock()
        self.mock_cursor = self.mock_conn.cursor.return_value
        mock_connect.return_value = self.mock_conn
        self.data_soucre = DataSource()

    def test_meeting_page(self):
        """Tests a correct path that should display the methods result"""
        self.data_soucre.connection.cursor().fetchall.return_value = [[1.6357466063348416]]
        response = self.app.post("/search", data={
            "search": "meetings",
        })
        self.assertIn(
            b'li>Average meetings attended by study participants: 1.64</li>' +
            b'\n                <li>Average frequency of meeting attendance by study ' +
            b'participants: 100.0%</li>',
            response.data,
        )

    def test_drug_sale_result_page(self):
        """Test for route for drug sale arrests"""
        self.data_soucre.connection.cursor().fetchall.return_value = (
            [None]*283
            )
        response = self.app.post("/search", data={
            "search": "arrests",
        })
        self.assertIn(
            b'Please enter your lower and upper bounds as directed',
                          response.data)

    def test_home_page(self):
        """Test for route for home page"""
        self.data_soucre.connection.cursor().fetchall.return_value = (
            [None]*283
            )
        response = self.app.post("/search", data={
            "search": "home",
        })
        self.assertIn(
            b'<h2>Info:</h2>',
                response.data)

    def test_data_overview_page(self):
        """Test for route for home page"""
        self.data_soucre.connection.cursor().fetchall.return_value = (
            [[1]]*2
            )
        response = self.app.post("/search", data={
            "search": "data_overview",
        })
        self.assertIn(
            b'<h2 id="exclusive">Data Overview</h2>',
            response.data
            )
