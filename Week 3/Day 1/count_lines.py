# Write a function that takes a filename as string,
# then returns the number of lines the file contains.
# It should return zero if it can't open the file, and
# should not raise any error.

def line_counter(filename):
    try:
        open(filename, "r")
        num_lines = sum(1 for line in open(filename))
        print(num_lines)
    except FileNotFoundError:
        print("0")

filename = input("Please provide the filename here: ")

line_counter(filename)