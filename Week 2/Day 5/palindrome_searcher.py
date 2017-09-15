# Create a function named search palindrome following your current language's style guide. It should take a string, search for palindromes
# that at least 3 characters long and return a list with the found palindromes.

# Examples

# input	output
# "dog goat dad duck doodle never"	["og go", "g g", " dad ", "dad", "d d", "dood", "eve"]
# "apple"	[]
# "racecar"	["racecar"]
# ""	[]

def search_palindrome(sentence):
    found_palindrome = []
    reverse = reverser(sentence)
    length = len(sentence)
    for i in range(length -2):
        for j in range (3, length +1):
            if sentence[i:i+j] == reverse[length-(i+j): length-i]:
                found_palindrome.append(sentence[i:i+j])
    return found_palindrome


def reverser(sentence):
    sentence = list(sentence)
    reverse = sentence[::-1]
    reverse = ''.join(reverse)
    return reverse


sentence = input("Hello! This is a palindrome program. To find all the palindromes in a  sentence, enter your sentence here!: ")

print(search_palindrome(sentence))
