# Accidentally I messed up this quote from Richard Feynman.
# Two words are out of place
# Your task is to fix it by swapping the right words with code

# Also, print the sentence to the output with spaces in between.
import random

words = ["What", "I", "do", "create,", "I", "cannot", "not", "understand."]

space = " "

def change_words(anything):
    temp = []
    temp = words[5]
    words[5] = words[2]
    words[2] = temp
    return words

def making_sentence(anything):
    sentence = ""
    for num in range(len(anything)):
        sentence += words[num] + space
    return sentence

correct_order = change_words(words)
print (making_sentence(words))