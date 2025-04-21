import fileinput

data = []
dataInitalized = False

def meeting_frequency():
    initialize_data()
    attendance = get_col(get_col_num_with_title("NSHLPM"))
    return "Not implemented yet"

def meeting_count():
    initialize_data()
    attendance = get_col(get_col_num_with_title("NSHLPM"))
    return get_sum(attendance)/(len(attendance)-1)

def drug_sale_arrests(lower, upper):
    initialize_data()
    return "Not implemented yet"

def make_data_array():
    for line in fileinput.input(
        files=('Data/ICPSR_30842/DS0001/30842-0001-Data.tsv'), encoding="utf-8"):
        data.append(line.split("\t"))

def initialize_data():
    global dataInitalized
    if not dataInitalized:
        make_data_array()
        dataInitalized = True

def get_col_num_with_title(name):
    i = 0
    for s in data[0]:
        if name == s:
            return i
        i += 1
    return -1

def get_sum(arr):
    sum = 0
    for i in arr:
        try:
            sum += int(i)
        except ValueError:
            sum += 0
    return sum

def get_col(num):
    temp = []
    for i in range(1, len(data)):
        temp.append(data[i][num])
    return temp
