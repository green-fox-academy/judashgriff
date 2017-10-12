# Create a function called `unique_characters` that takes a string as parameter
# and returns a list with the unique letters of the given string
# Create basic unit tests for it with at least 3 different test cases
# print(unique_characters("anagram"))
# Should print out:
# ["n", "g", "r", "m"]

def count_chars(string):
    my_list = {}
    for char in list(string):
        if char not in my_list:
            my_list[char] = 1
        else: 
            my_list[char] += 1
    return (unique_characters(my_list))

def unique_characters(my_list):
    to_return = []
    for key, value in my_list.items():
        if value == 1:
            to_return.append(key)
    return to_return

print(count_chars("anagram"))