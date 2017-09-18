# Find the substring in the list

# Create a function that takes a string and a list of string as a parameter
# Returns the index of the string in the list where the first string is part of
# Returns -1 if the string is not part any of the strings in the list
# Example

# input: "ching", ["this", "is", "what", "I'm", "searching", "in"]
# output: 4

def find_str(input1, the_string):
    the_list = make_list(input1)
    for i in the_list:
        if the_string in i:
            print(the_list.index(i))
    return

def make_list(input1):
    the_list = []
    the_list += input1.split(" ")
    return the_list



input1 = input("Please enter a list of words!: ")
input2 = input("Please enter a word you are looking for!: ")

find_str(input1, input2)