# Check if list contains all of the following elements: 4,8,12,16
# Create a function that accepts list_of_numbers as an input
# it should return "True" if it contains all, otherwise "False"

my_list = [4,8,12,16]
list_of_numbers = [2, 4, 6, 8, 10, 12, 14, 16]

def is_all_elements_in(my_list, list_of_numbers):
    for element in my_list:
        if not element in list_of_numbers:
            return False
    return True
    
print(is_all_elements_in(my_list, list_of_numbers))