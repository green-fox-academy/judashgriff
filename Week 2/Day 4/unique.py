# Unique - remove the duplicates

#  -  Create a function that takes a list of numbers as a parameter
#  -  Returns a list of numbers where every number in the list occurs only once

#  ## Example
#  -  input: `[1, 11, 34, 11, 52, 61, 1, 34]`
#  -  output: `[1, 11, 34, 52, 61]`


user_list = input("Please provide a list of numbers by your choice: ")

makeshift_list = user_list.split(" ")

final = sorted(set(dict.fromkeys(makeshift_list)))
print(final)