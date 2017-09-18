# Create a function that takes 3 parameters: a path, a word and a number,
# than it should write to a file.
# The path parameter should be a string, that describes the location of the file.
# The word parameter should be a string, that will be written to the file as lines
# The number paramter should describe how many lines the file should have.
# So if the word is "apple" and the number is 5, than it should write 5 lines
# to the file and each line should be "apple"
# The function should not raise any error if it could not write the file.


def function(path, word, number):
    try:
        file = open(path, "w")
        file.write((word + "\n") * number)
        file.close()
        return
    except:
        print("No luck, dude!")
        return

path = input("Hello! Please provide a path to the file you want to write into!\n")
word = input("What do you want to write into the file?\n")
number = int(input("How many lines the file should have? Each will have your input in it.\n"))

function(path, word, number)