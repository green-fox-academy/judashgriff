# # Find part of an integer

#  -  Create a function that takes two strings as a parameter
#  -  Returns the starting index where the second one is starting in the first one
#  -  Returns `-1` if the second string is not in the first one

#  ## Example
#  -  input: `"this is what I'm searching in"`, `"searching"`
#  -  output: `17`


def lowercase(string):
    lowercase = ""
    lowercase += string.lower()
    return lowercase


def string_search(first, second):
    match = ""
    first_lower = lowercase(first)
    second_lower = lowercase(second)
    if second_lower in first_lower:
        return first_lower.index(second_lower[0])
    else:
        return (-1)


input1 = input("Please enter a sentence!: ")
input2 = input("Please enter a word from the previous sentence!: ")

print(string_search(input1, input2))