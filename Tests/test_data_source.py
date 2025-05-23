"""Test code for data source app"""

import unittest
from unittest.mock import MagicMock, patch
from ProductionCode.datasource import DataSource, process_graph_data


class TestGetMeetingsAttended(unittest.TestCase):
    """Tests the path based method calls and pages"""

    def setUp(self):
        #create a mock connection and cursor
        self.mock_conn = MagicMock()
        self.mock_cursor = self.mock_conn.cursor.return_value

    @patch('ProductionCode.datasource.psycopg2.connect')
    def test_route(self, mock_connect):
        """Tests a correct path that should display the methods result"""
        mock_connect.return_value = self.mock_conn
		#set what it should return
        self.mock_cursor.fetchall.return_value = (
            [[1.6357466063348416]]
            )
        data_soucre = DataSource()
        self.assertEqual(
            data_soucre.get_ave_meetings_attended(),
            1.64
        )

class TestGetArrestRanges(unittest.TestCase):
    """Tests the path based method calls and pages"""

    def setUp(self):
        #create a mock connection and cursor
        self.mock_conn = MagicMock()
        self.mock_cursor = self.mock_conn.cursor.return_value

    @patch('ProductionCode.datasource.psycopg2.connect')
    def test_route(self, mock_connect):
        """Tests a correct path that should display the methods result"""
        mock_connect.return_value = self.mock_conn
		#set what it should return
        self.mock_cursor.fetchall.return_value = (
            [None]*283
            )
        data_soucre = DataSource()
        self.assertEqual(
            data_soucre.get_arrest_ranges(1, 10),
            283
        )

class TestGetHealthData(unittest.TestCase):
    """Tests the path based method calls and pages"""

    @patch('ProductionCode.datasource.psycopg2.connect')
    def test_route(self, mock_connect):
        """Tests a correct path that should display the methods result"""
        mock_connect.return_value = self.mock_conn
		#set what it should return
        self.mock_cursor.fetchall.return_value = (
            [None]*283
            )
        data_soucre = DataSource()
        self.assertEqual(
            data_soucre.get_alcohol_physical_health
            283
        )

class TestGetGraphData(unittest.TestCase):
    """Tests the path based method calls and pages"""

    def setUp(self):
        #create a mock connection and cursor
        self.mock_conn = MagicMock()
        self.mock_cursor = self.mock_conn.cursor.return_value

    @patch('ProductionCode.datasource.psycopg2.connect')
    def test_route(self, mock_connect):
        """Tests a correct path that should display the methods result"""
        mock_connect.return_value = self.mock_conn
		#set what it should return
        self.mock_cursor.fetchall.return_value = (
            [[1]]*2
            )
        data_soucre = DataSource()
        self.assertEqual(
            data_soucre.get_graph_data(),
            [[1, 1], [1, 1]]
        )

class TestProcessGraphData(unittest.TestCase):
    """Tests the graph data combining function"""

    def test_list_combine(self):
        """Tests that the two list are combiend correctly"""
        self.assertEqual(process_graph_data([[1], [2], [3]], [[0], [0], [0]]),
                         [[1, 0], [2, 0], [3, 0]])
