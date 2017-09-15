# Create a function named is anagram following your current language's style guide. It should take two inputings and return a boolean value 
# depending on whether its an anagram or not.

# Examples

# input 1	input 2	output
# "dog"	"god"	true
# "green"	"fox"	false

def is_anagram(input1, input2):
    input1_list = list(input1)
    input1_list.sort()
    input2_list = list(input2)
    input2_list.sort()

    return (input1_list == input2_list)



input1 = input("Please provide a word: ")
input2 = input("Please provide a second word: ")

print(is_anagram(input1, input2))

