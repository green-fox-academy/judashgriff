# Create a function named create palindrome following your current language's style guide. It should take a string, create a palindrome from 
# it and then return it.

# Examples

# input	output
# ""	""
# "greenfox"	"greenfoxxofneerg"
# "123"	"123321"

def palindrome(sentence):
    palindrome_sentence = sentence[::-1]
    return (sentence == sentence[::-1]), palindrome_sentence 


def make_palindrome_anyway(sentence):
    palindrome_sentence = sentence + sentence[::-1]
    return palindrome_sentence


sentence = input("Hello! This is a palindrome program. To find out if a sentence is palindrome, enter your sentence here!: ")
print(palindrome(sentence))

print(make_palindrome_anyway(sentence))