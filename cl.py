"""Code for the Command Line Interface"""

import sys
from ProductionCode import data_procesor


def main():
    """Runs the Program"""
    process_input()


def process_input():
    """Takes in the command line input and calls
    the methods from production code to get the requested info"""
    if len(sys.argv) == 0:
        print_usage_statement()
    elif len(sys.argv) > 1 and sys.argv[1] == "--meeting":
        input_meeting_helper()
    elif len(sys.argv) > 1 and sys.argv[1] == "--sellArrests":
        input_serrest_helper()
    else:
        print_usage_statement()


def input_meeting_helper():
    """Serves as a helper for calling the production code method meeting_frequency/count()"""
    if len(sys.argv) == 3:
        if sys.argv[2] == "frequency" or sys.argv[2] == "freq":
            print(str(data_procesor.meeting_frequency()) + "%")
        if sys.argv[2] == "count":
            print(str(data_procesor.meeting_count()) + " meetings attended")
    else:
        print_usage_statement()


def input_serrest_helper():
    """Serves as a helper for calling the production code method drug_sale_arrests()"""
    if get_sys_argv_length() == 4:
        try:
            print(
                str(
                    data_procesor.drug_sale_arrests(
                        int(sys.argv[2]), int(sys.argv[3])
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
        '\npython3 cl.py --meeting ["frequency", "count"]'
        "\npython3 cl.py --sellArrests lowerBoundCount upperBoundCount"
    )


if __name__ == "__main__":
    main()
