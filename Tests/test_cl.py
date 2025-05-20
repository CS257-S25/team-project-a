"""Test code for command line interface"""

import unittest
import sys
from io import StringIO
from unittest.mock import MagicMock, patch
import cl

dummyData = [
    ["NSHLPM", "ARSTDRUG"],
    ["3", "1"],
    ["20", "6"],
    ["4", "15"],
    ["0", "9"],
    [" ", " "],
]


class TestProcessInput(unittest.TestCase):
    """Testing the get_cell method"""

    def setUp(self):
        """Sets up the dummy data"""
        self.mock_conn = MagicMock()
        self.mock_cursor = self.mock_conn.cursor.return_value

    @patch('ProductionCode.datasource.psycopg2.connect')
    def test_meeting_command_line_freq(self, mock_connect):
        """Testing that the comand line command returns something when valid"""
        sys.argv = ["basic_cl.py", "--meeting-freq"]
        mock_connect.return_value = self.mock_conn
		#set what it should return
        self.mock_cursor.fetchall.return_value = (
            [[32.71]]
            )
        sys.stdout = StringIO()
        cl.main()
        printed_output = sys.stdout.getvalue().strip()
        self.assertEqual(printed_output, "100.0%", "should be 100.0%")

    @patch('ProductionCode.datasource.psycopg2.connect')
    def test_meeting_command_line_count(self, mock_connect):
        """Testing that the comand line command returns something when valid"""
        sys.argv = ["basic_cl.py", "--meeting-count"]
        mock_connect.return_value = self.mock_conn
		#set what it should return
        self.mock_cursor.fetchall.return_value = (
            [[1.6357466063348416]]
            )
        sys.stdout = StringIO()
        cl.main()
        printed_output = sys.stdout.getvalue().strip()
        self.assertEqual(
            printed_output, "1.64 meetings attended", "should be 1.64 meetings attended"
        )

    @patch('ProductionCode.datasource.psycopg2.connect')
    def test_arrests_command_line(self, mock_connect):
        """Testing that the comand line command returns something when valid"""
        sys.argv = ["basic_cl.py", "--sell-arrests", 1, 10]
        mock_connect.return_value = self.mock_conn
		#set what it should return
        self.mock_cursor.fetchall.return_value = (
            [None]*283
            )
        sys.stdout = StringIO()
        cl.main()
        printed_output = sys.stdout.getvalue().strip()
        self.assertEqual(printed_output, "283 people", "should be 283 people")

    def test_command_line_no_input(self):
        """Testing that the comand line command returns the usage case
        when invalid input is passed in"""
        sys.argv = []
        sys.stdout = StringIO()
        cl.main()
        printed_output = sys.stdout.getvalue().strip()
        self.assertEqual(
            printed_output,
            "Usage:"
            "\npython3 cl.py --meeting-frequency"
            "\npython3 cl.py --meeting-count"
            "\npython3 cl.py --sellArrests lowerBoundCount upperBoundCount",
            "Should be Usage:"
            "\npython3 cl.py --meeting-frequency"
            "\npython3 cl.py --meeting-count"
            "\npython3 cl.py --sellArrests lowerBoundCount upperBoundCount",
        )

    def test_arrests_command_line_wrong_input(self):
        """Testing that the comand line command returns the usage case
        when invalid input is passed in"""
        sys.argv = ["basic_cl.py", "--sell-arrests"]
        sys.stdout = StringIO()
        cl.main()
        printed_output = sys.stdout.getvalue().strip()
        self.assertEqual(
            printed_output,
            "Usage:"
            "\npython3 cl.py --meeting-frequency"
            "\npython3 cl.py --meeting-count"
            "\npython3 cl.py --sellArrests lowerBoundCount upperBoundCount",
            "Should be Usage:"
            "\npython3 cl.py --meeting-frequency"
            "\npython3 cl.py --meeting-count"
            "\npython3 cl.py --sellArrests lowerBoundCount upperBoundCount",
        )

    def test_arrests_command_line_bad_input(self):
        """Testing that the comand line command returns the usage case
        when invalid input is passed in"""
        sys.argv = ["basic_cl.py", "--sell-arrests", "sbjs", "202"]
        sys.stdout = StringIO()
        cl.main()
        printed_output = sys.stdout.getvalue().strip()
        self.assertEqual(
            printed_output,
            "Usage:"
            "\npython3 cl.py --meeting-frequency"
            "\npython3 cl.py --meeting-count"
            "\npython3 cl.py --sellArrests lowerBoundCount upperBoundCount",
            "Should be Usage:"
            "\npython3 cl.py --meeting-frequency"
            "\npython3 cl.py --meeting-count"
            "\npython3 cl.py --sellArrests lowerBoundCount upperBoundCount",
        )

    def test_meetings_command_line_wrong_input(self):
        """Testing that the comand line command returns the usage case
        when invalid input is passed in"""
        sys.argv = ["basic_cl.py", "--meetings"]
        sys.stdout = StringIO()
        cl.main()
        printed_output = sys.stdout.getvalue().strip()
        self.assertEqual(
            printed_output,
            "Usage:"
            "\npython3 cl.py --meeting-frequency"
            "\npython3 cl.py --meeting-count"
            "\npython3 cl.py --sellArrests lowerBoundCount upperBoundCount",
            "Should be Usage:"
            "\npython3 cl.py --meeting-frequency"
            "\npython3 cl.py --meeting-count"
            "\npython3 cl.py --sellArrests lowerBoundCount upperBoundCount",
        )

    def test_command_line_wrong_input(self):
        """Testing that the comand line command returns the usage case
        when invalid input is passed in"""
        sys.argv = ["basic_cl.py"]
        sys.stdout = StringIO()
        cl.main()
        printed_output = sys.stdout.getvalue().strip()
        self.assertEqual(
            printed_output,
            "Usage:"
            "\npython3 cl.py --meeting-frequency"
            "\npython3 cl.py --meeting-count"
            "\npython3 cl.py --sellArrests lowerBoundCount upperBoundCount",
            "Should be Usage:"
            "\npython3 cl.py --meeting-frequency"
            "\npython3 cl.py --meeting-count"
            "\npython3 cl.py --sellArrests lowerBoundCount upperBoundCount",
        )


class TestGetSysArgvLength(unittest.TestCase):
    """Testing the get_sys_argv_length method"""

    def test_normal_input(self):
        """Tests that the argv length is correct for a normal command line call"""
        sys.argv = ["cl.py", "--meeting", "freq"]
        self.assertEqual(cl.get_sys_argv_length(), 3, "Should be 3")

    def test_no_input(self):
        """Tests that the argv length is correct for a incorrect command line call"""
        sys.argv = ["cl.py"]
        self.assertEqual(cl.get_sys_argv_length(), 1, "Should be 1")


class TestPrintUsageStatement(unittest.TestCase):
    """Testing the usage statement"""

    def test_usage_statement(self):
        """Tests that the usage statement is printed"""
        sys.stdout = StringIO()
        cl.print_usage_statement()
        printed_output = sys.stdout.getvalue().strip()
        self.assertEqual(
            printed_output,
            "Usage:"
            "\npython3 cl.py --meeting-frequency"
            "\npython3 cl.py --meeting-count"
            "\npython3 cl.py --sellArrests lowerBoundCount upperBoundCount",
            "Should be Usage:"
            "\npython3 cl.py --meeting-frequency"
            "\npython3 cl.py --meeting-count"
            "\npython3 cl.py --sellArrests lowerBoundCount upperBoundCount",
        )


if __name__ == "__main__":
    unittest.main()
