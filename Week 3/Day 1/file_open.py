# Write a program that opens a file called "my-file.txt", then prints
# each of lines form the file.
# If the program is unable to read the file (for example it does not exists),
# then it should print an error message like: "Unable to read file: my-file.txt"

def open_file(filename):
    try:
        open(filename, "r")
        print(filename.read())
    except:
        return "Unable to read file: my-file.txt"


print(open_file("my-file.txt"))