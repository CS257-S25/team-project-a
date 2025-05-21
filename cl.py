"""Code for the Command Line Interface"""

import sys
from ProductionCode.datasource import DataSource


def main():
    """Runs the Program"""
    process_input()


def process_input():
    """Takes in the command line input and calls
    the methods from production code to get the requested info"""
    if len(sys.argv) == 0:
        print_usage_statement()
    elif len(sys.argv) > 1 and sys.argv[1].startswith("--meeting"):
        input_meeting_helper(sys.argv[1])
    elif len(sys.argv) > 1 and sys.argv[1] == "--sellArrests":
        input_serrest_helper()
    else:
        print_usage_statement()


def input_meeting_helper(arg):
    """Serves as a helper for calling the production code method meeting_frequency/count()"""
    args = arg.split("-")[2:]
    if len(args) == 2:
        if args[1] == "frequency" or args[1] == "freq":
            data_source = DataSource()
            print(str(data_source.get_freq_meetings_attended()) + "%")
        if args[1] == "count":
            data_source = DataSource()
            print(str(data_source.get_ave_meetings_attended()) + " meetings attended")
    else:
        print_usage_statement()


def input_serrest_helper():
    """Serves as a helper for calling the production code method drug_sale_arrests()"""
    if get_sys_argv_length() == 4:
        try:
            low = int(sys.argv[2])
            high = int(sys.argv[3])
            data_source = DataSource()
            print(
                str(
                    data_source.get_arrest_ranges(
                        low, high
                    )
                )
                + " people"
            )
        except ValueError:
            print_usage_statement()
    else:
        print_usage_statement()


def get_sys_argv_length():
    """gives the numebr of commands in the comand line input"""
    return len(sys.argv)


def print_usage_statement():
    """Prints the class usage statement when improper input is given"""
    print(
        "Usage:"
        '\npython3 cl.py --meeting-frequency'
        '\npython3 cl.py --meeting-count'
        "\npython3 cl.py --sellArrests lowerBoundCount upperBoundCount"
    )


if __name__ == "__main__":
    main()
