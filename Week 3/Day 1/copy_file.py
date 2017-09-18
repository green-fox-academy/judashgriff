# Write a function that copies a file to an other
# It should take the filenames as parameters
# It should return a boolean that shows if the copy was successful

def copy(file1, file2):
    try:
        with open(file1) as f:
            lines = f.readlines()
            print(lines)
            with open(file2, "w") as f1:
                f1.writelines(lines)
        return True
    except: 
        return False


first = input("Yo, what is the file you wanna copy to anada?\n")
second = input("Yo, what is the file you wanna copy to?\n")


print(copy(first, second))