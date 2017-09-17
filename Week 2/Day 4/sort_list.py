# # Sort that list

#  -  Create a function that takes a list of numbers as parameter
#  -  Returns a list where the elements are sorted in ascending numerical order
#  -  Make a second boolean parameter, if it's `true` sort that list descending

#  ## Example
#  -  input `[34, 12, 24, 9, 5]`
#  -  output `[5, 9, 12, 24, 34]`


def separate_input_to_list(item):
    numbers_list = []
    numbers_list += item.split(" ")
    return ascend_numbers(numbers_list)


def ascend_numbers(user_list):
    user_list.sort(key=int)
    return user_list

def descend_numbers(user_list):
    if True:
       user_list.sort(key=int)
       print(user_list)
       return
    else:
        ascend_numbers(user_list)
    return


List = input("Please provide a list of numbers separated with a space!: ")

print(separate_input_to_list(List))
