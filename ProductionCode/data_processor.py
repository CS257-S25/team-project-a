"""Gathers the data into a 2d array and parses through it based on user requests"""

from ProductionCode import data

data_obj = data.Data()

def meeting_frequency():
    """returns the avegrage frequency of meeting attendance by the subjects"""
    attendance = get_col(get_col_num_with_title("NSHLPM"))
    return round(((get_sum_array(attendance)/(get_total_valid(attendance)))/
                  get_max_num(attendance))*100, 2)

def meeting_count():
    """returns the avegrage count of meetings attended by the subjects"""
    attendance = get_col(get_col_num_with_title("NSHLPM"))
    return round(get_sum_array(attendance)/(get_total_valid(attendance)), 2)

def drug_sale_arrests(lower, upper):
    """returns the number of subjects arrested on drug charges a number of times 
    in the range lower-upper"""
    arrests = get_col(get_col_num_with_title("ARSTDRUG"))
    return get_total_count_in_range(arrests, lower, upper)


def get_col_num_with_title(name):
    """gets a columns index out of the data set with a specific variable name"""
    i = 0
    for s in data_obj.data[0]:
        if name == s:
            return i
        i += 1
    return -1

def get_sum_array(arr):
    """gets the sum of a string array of numbers"""
    temp = 0
    for i in arr:
        try:
            temp += int(i)
        except ValueError:
            temp += 0
    return temp

def get_max_num(arr):
    """gets the maximum number in a string array of numbers"""
    temp = 0
    for i in arr:
        try:
            temp = max(temp, int(i))
        except ValueError:
            pass
    return temp

def get_total_valid(arr):
    """gets the total valid numbers in a string array of numbers"""
    count = 0
    for i in arr:
        try:
            int(i)
            count += 1
        except ValueError:
            pass
    return count

def get_total_count_in_range(arr, lower, upper):
    """gets the count of numbers within a certain range in a string array of numbers"""
    count = 0
    for i in arr:
        try:
            if int(i) >= lower and int(i) <= upper:
                count += 1
        except ValueError:
            pass
    return count

def get_col(num):
    """gets a column with a specific index out of a 2d array"""
    temp = []
    for i in range(1, len(data_obj.data)):
        temp.append(data_obj.data[i][num])
    return temp
