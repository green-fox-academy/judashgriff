# # Find the part of int

#  -  Create a function that takes a number and a list of numbers as a parameter
#  -  Returns the indeces of the numbers in the list where the first number is part of
#  -  Returns an empty list if the number is not part any of the numbers in the list

#  ## Example
#  -  input: `[1, 11, 34, 52, 61]`, `1`
#  -  output: `[0, 1, 4]`

def find_int(input1, the_number):
    the_list = make_numbers(input1)
    for i in range(len(the_list)):
        if the_number in the_list[i]:
            print(i)
    return


def make_numbers(input1):
    the_list = input1.split(" ")
    # the_list = list(map(int, the_list))
    print(the_list)
    return the_list


input1 = input("Please enter a list of numbers!: ")
input2 = input("Please enter a number you are looking for!: ")

find_int(input1, input2)