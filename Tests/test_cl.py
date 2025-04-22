"""Test code"""

import unittest
import sys
from io import StringIO
from ProductionCode import data_procesor
import cl

dummyData = [
    ["NSHLPM", "ARSTDRG"],
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
        data_procesor.initalize_dummy_data(dummyData)

    def test_meeting_command_line_freq(self):
        """Testing that the comand line command returns something when valid"""
        sys.argv = ["basic_cl.py", "--meeting", "freq"]
        sys.stdout = StringIO()
        cl.main()
        printed_output = sys.stdout.getvalue().strip()
        self.assertEqual(printed_output, "33.75%", "should be 33.75%")

    def test_meeting_command_line_count(self):
        """Testing that the comand line command returns something when valid"""
        sys.argv = ["basic_cl.py", "--meeting", "count"]
        sys.stdout = StringIO()
        cl.main()
        printed_output = sys.stdout.getvalue().strip()
        self.assertEqual(
            printed_output, "6.75 meetings attended", "should be 6.75 meetings attended"
        )

    def test_arrests_command_line(self):
        """Testing that the comand line command returns something when valid"""
        sys.argv = ["basic_cl.py", "--sellArrests", 1, 10]
        sys.stdout = StringIO()
        cl.main()
        printed_output = sys.stdout.getvalue().strip()
        self.assertEqual(printed_output, "3 people", "should be 3 people")

    def test_arrests_command_line_wrong_input(self):
        """Testing that the comand line command returns the usage case 
        when invalid input is passed in"""
        sys.argv = ["basic_cl.py", "--sellArrests"]
        sys.stdout = StringIO()
        cl.main()
        printed_output = sys.stdout.getvalue().strip()
        self.assertEqual(
            printed_output,
            "Usage:"
            '\npython3 cl.py --meeting ["frequency", "count"]'
            "\npython3 cl.py --sellArrests lowerBoundCount upperBoundCount",
            "Should be Usage:"
            '\npython3 cl.py --meeting ["frequency", "count"]'
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
            '\npython3 cl.py --meeting ["frequency", "count"]'
            "\npython3 cl.py --sellArrests lowerBoundCount upperBoundCount",
            "Should be Usage:"
            '\npython3 cl.py --meeting ["frequency", "count"]'
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
            '\npython3 cl.py --meeting ["frequency", "count"]'
            "\npython3 cl.py --sellArrests lowerBoundCount upperBoundCount",
            "Should be Usage:"
            '\npython3 cl.py --meeting ["frequency", "count"]'
            "\npython3 cl.py --sellArrests lowerBoundCount upperBoundCount",
        )


class TestMeetingFrequency(unittest.TestCase):
    """Testing the get_row_titles method"""

    def setUp(self):
        """Sets up the dummy data"""
        data_procesor.initalize_dummy_data(dummyData)

    def test_meeting_frequency(self):
        """Checks that the meeting frequency is returned"""
        self.assertEqual(data_procesor.meeting_frequency(), 33.75, "Should be 33.75")


class TestMeetingCount(unittest.TestCase):
    """Testing the get_row_by_titles method"""

    def setUp(self):
        """Sets up the dummy data"""
        data_procesor.initalize_dummy_data(dummyData)

    def test_meeting_count(self):
        """Checks that the meeting frequency is returned"""
        self.assertEqual(data_procesor.meeting_count(), 6.75, "Should be 6.75")


class TestDrugSaleArrests(unittest.TestCase):
    """Testing the get_silly method"""

    def setUp(self):
        """Sets up the dummy data"""
        data_procesor.initalize_dummy_data(dummyData)

    def test_normal_range(self):
        """Checks that the meeting frequency is returned"""
        self.assertEqual(data_procesor.drug_sale_arrests(1, 10), 3, "Should be 3")

    def test_small_range(self):
        """Checks that the meeting frequency is returned"""
        self.assertEqual(data_procesor.drug_sale_arrests(2, 4), 0, "Should be 0")

    def test_big_range(self):
        """Checks that the meeting frequency is returned"""
        self.assertEqual(data_procesor.drug_sale_arrests(0, 30), 4, "Should be 4")


class TestGetColNumWithTitle(unittest.TestCase):
    """Testing the get_col_num_with_title method"""

    def setUp(self):
        """Sets up the dummy data"""
        data_procesor.initalize_dummy_data(dummyData)

    def test_correct_name(self):
        """Testing that for a correct name input it returns the correct column"""
        self.assertEqual(
            data_procesor.get_col_num_with_title("NSHLPM"), 0, "should be 0"
        )

    def test_incorrect_name(self):
        """Testing that for a incorrect name input it returns -1"""
        self.assertEqual(
            data_procesor.get_col_num_with_title("AAAA"), -1, "should be -1"
        )


class TestGetSum(unittest.TestCase):
    """Testing the get_sum method"""

    def test_correct_values(self):
        """Testing that for a correct values the sum is output"""
        self.assertEqual(data_procesor.get_sum(["1", "2", "3"]), 6, "should be 6")

    def test_incorrect_value(self):
        """Testing that for incorrect values the sum is unchanhged"""
        self.assertEqual(
            data_procesor.get_sum(["1", "2", "3", "value"]),
            6,
            "should be 6",
        )

    def test_blank_value(self):
        """Testing that for incorrect values the sum is unchanhged"""
        self.assertEqual(data_procesor.get_sum(["1", "2", "3", ""]), 6, "should be 6")


class TestGetMax(unittest.TestCase):
    """Testing the get_max method"""

    def test_correct_values(self):
        """Testing that for a correct values the max is output"""
        self.assertEqual(data_procesor.get_max(["1", "2", "3"]), 3, "should be 3")

    def test_incorrect_value(self):
        """Testing that for incorrect values the max is unchanhged"""
        self.assertEqual(
            data_procesor.get_max(["1", "2", "3", "value"]),
            3,
            "should be 3",
        )

    def test_blank_value(self):
        """Testing that for incorrect values the max is unchanhged"""
        self.assertEqual(data_procesor.get_max(["1", "2", "3", ""]), 3, "should be 3")


class TestGetTotalValid(unittest.TestCase):
    """Testing the get_total_valid_method"""

    def test_correct_values(self):
        """Testing that for a correct values the valid cell count is output"""
        self.assertEqual(
            data_procesor.get_total_valid(["1", "2", "3"]), 3, "should be 3"
        )

    def test_incorrect_value(self):
        """Testing that for incorrect values the valid cell count is unchanhged"""
        self.assertEqual(
            data_procesor.get_total_valid(["1", "2", "3", "value"]),
            3,
            "should be 3",
        )

    def test_blank_value(self):
        """Testing that for incorrect values the valid cell count is unchanhged"""
        self.assertEqual(
            data_procesor.get_total_valid(["1", "2", "3", ""]), 3, "should be 3"
        )


class TestGetTotalCountInRange(unittest.TestCase):
    """Testing the get_count_in_range_method"""

    def test_correct_values(self):
        """Testing that for a correct values the sum is output"""
        self.assertEqual(
            data_procesor.get_total_count_in_range(["1", "2", "3"], 1, 2),
            2,
            "should be 2",
        )

    def test_correct_values_large_range(self):
        """Testing that for a correct values the sum is output"""
        self.assertEqual(
            data_procesor.get_total_count_in_range(["1", "2", "3"], -1, 20),
            3,
            "should be 3",
        )

    def test_incorrect_value(self):
        """Testing that for incorrect values the sum is unchanhged"""
        self.assertEqual(
            data_procesor.get_total_count_in_range(["1", "2", "3", "value"], 1, 2),
            2,
            "should be 2",
        )

    def test_blank_value(self):
        """Testing that for incorrect values the sum is unchanhged"""
        self.assertEqual(
            data_procesor.get_total_count_in_range(["1", "2", "3", ""], 1, 2),
            2,
            "should be 2",
        )


class TestGetCol(unittest.TestCase):
    """Testing the get_col method"""

    def setUp(self):
        """Sets up the dummy data"""
        data_procesor.initalize_dummy_data(dummyData)

    def test_correct_name(self):
        """Testing that for a correct name input it returns the correct column"""
        self.assertEqual(
            data_procesor.get_col(1),
            ["1", "6", "15", "9", " "],
            'should be ["1", "6", "15", "9", " "]',
        )

    def test_incorrect_column_index(self):
        """Testing that for a incorrect name input it returns -1"""
        self.assertRaises(IndexError, data_procesor.get_col, sys.maxsize)


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
            '\npython3 cl.py --meeting ["frequency", "count"]'
            "\npython3 cl.py --sellArrests lowerBoundCount upperBoundCount",
            "Should be Usage:"
            '\npython3 cl.py --meeting ["frequency", "count"]'
            "\npython3 cl.py --sellArrests lowerBoundCount upperBoundCount",
        )


if __name__ == "__main__":
    unittest.main()
