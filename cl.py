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
    elif len(sys.argv) > 1:
        if sys.argv[1] == "--meeting":
            if len(sys.argv) == 3:
                if sys.argv[2] == "frequency" or sys.argv[2] == "freq":
                    print(data_procesor.meeting_frequency())
                if sys.argv[2] == "count":
                    print(data_procesor.meeting_count())
            else:
                print_usage_statement()
        elif sys.argv[1] == "--sellArrest":
            if get_sys_argv_length() == 4:
                try:
                    data_procesor.drug_sale_arrests(int(sys.argv[2]), int(sys.argv[3]))
                except ValueError:
                    print_usage_statement()
            else:
                print_usage_statement()
        else:
            print_usage_statement()
    else:
        print_usage_statement()

def get_sys_argv_length():
    """gives the numebr of commands in the comand line input"""
    return len(sys.argv)

def print_usage_statement():
    """Prints the class usage statement when improper input is given"""
    print("Usage:" \
    "\npython3 --meeting [\"frequency\", \"count\"]" \
    "\npython3 --sellArrests lowerBoundCount UpperBoundCount")

if __name__=="__main__":
    main()
