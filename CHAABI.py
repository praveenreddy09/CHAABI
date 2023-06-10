#QUESTION 1

def selection_sort(arr):
    # Traverse through all array elements
    for i in range(len(arr)):
        # Find the minimum element in the remaining unsorted part
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap the found minimum element with the first element
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr

# Test the function
input_list = [5, 416, 54, 21, 6135, 15, 741]
sorted_list = selection_sort(input_list)
print(sorted_list)


#QUESTION 2

def get_file_types(extension_type_list, filenames):
    # Create a dictionary to store the file types
    file_types = {}

    # Split the extension and type values
    extension_types = extension_type_list.split(";")
    extension_type_dict = {}
    for extension_type in extension_types:
        extension, file_type = extension_type.split(",")
        extension_type_dict[extension] = file_type

    # Iterate over the filenames and determine the file type
    for filename in filenames:
        # Get the file extension
        file_extension = filename.split(".")[-1]

        # Determine the file type from the extension
        if file_extension in extension_type_dict:
            file_types[filename] = extension_type_dict[file_extension]
        else:
            file_types[filename] = "unknown"

    return file_types

# Test the function
extension_type_list = "xls,spreadsheet;xlsx,spreadsheet;jpg,image"
filenames = ["abc.jpg", "xyz.xls", "text.csv", "123"]
result = get_file_types(extension_type_list, filenames)
print(result)



#QUESTION 3

def sort_list_of_dicts(list_of_dicts, key):
    sorted_list = sorted(list_of_dicts, key=lambda x: x[key])
    return sorted_list

# Test the function
input_list = [
    {"fruit": "orange", "color": "orange"},
    {"fruit": "apple", "color": "red"},
    {"fruit": "banana", "color": "yellow"},
    {"fruit": "blueberry", "color": "blue"}
]

sorted_list_by_fruit = sort_list_of_dicts(input_list, "fruit")
print(sorted_list_by_fruit)

sorted_list_by_color = sort_list_of_dicts(input_list, "color")
print(sorted_list_by_color)


#QUESTION 4

def switch_key_value(dictionary):
    return {v: k for k, v in dictionary.items()}

# Test the function
input_dict = {
    "key1": "value1",
    "key2": "value2",
    "key3": "value3",
    "key4": "value4",
    "key5": "value5"
}

result = switch_key_value(input_dict)
print(result)

#QUESTION 5


def compare_lists(list1, list2):
    common_elements = list(set(list1) & set(list2))
    non_common_elements = list(set(list1) ^ set(list2))
    return common_elements, non_common_elements

# Test the function
mainstream = ["One Punch Man", "Attack On Titan", "One Piece", "Sword Art Online", "Bleach", "Dragon Ball Z", "One Piece"]
must_watch = ["Full Metal Alchemist", "Code Geass", "Death Note", "Stein's Gate", "The Devil is a Part Timer!", "One Piece", "Attack On Titan"]

common, non_common = compare_lists(mainstream, must_watch)
print(common)
print(non_common)


#QUESTION 6


def get_every_other_sublist(lst, start_index, end_index):
    sublist = lst[start_index:end_index+1:2]
    return sublist

# Test the function
input_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]
start_index = 2
end_index = 9

result = get_every_other_sublist(input_list, start_index, end_index)
print(result)


#QUESTION 7

factorial = lambda n: 1 if n == 0 else n * factorial(n-1)

# Test the lambda function
number = 5
result = factorial(number)
print(result)


#QUESTION 8

A0 = dict(zip(('a', 'b', 'c', 'd', 'e'), (1, 2, 3, 4, 5)))
A1 = range(10)
A2 = sorted([i for i in A1 if i in A0])
A3 = sorted([A0[s] for s in A0])
A4 = [i for i in A1 if i in A3]
A5 = {i: i*i for i in A1}
A6 = [[i, i*i] for i in A1]
A7 = reduce(lambda x, y: x + y, [10, 23, -45, 33])
A8 = map(lambda x: x * 2, [1, 2, 3, 4])
A9 = filter(lambda x: len(x) > 3, ["I", "want", "to", "learn", "python"])

print("A0:", A0)
print("A1:", list(A1))
print("A2:", A2)
print("A3:", A3)
print("A4:", A4)
print("A5:", A5)
print("A6:", A6)
print("A7:", A7)
print("A8:", list(A8))
print("A9:", list(A9))



#QUESTION 9

from datetime import datetime, timedelta

def date_difference(from_date, to_date, difference):
    # Convert the date strings to datetime objects
    from_datetime = datetime.strptime(from_date, '%y-%m-%d')
    to_datetime = datetime.strptime(to_date, '%y-%m-%d')

    # Calculate the difference between the two dates
    delta = abs(from_datetime - to_datetime).days

    # Check if the difference is less than the specified difference
    if delta < difference:
        return True
    else:
        return False
    

#QUESTION 10

def f(x, l=[]):
    for i in range(x):
        l.append(i*i)
    print(l)

f(2)
f(3, [3, 2, 1])
f(3)



#THANK YOU