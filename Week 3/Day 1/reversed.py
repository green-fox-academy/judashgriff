# Create a method that decrypts reversed-lines.txt


def reverse(file_name):
    file = open(file_name, "r")
    out = open("ordered.txt", "w")
    for each in file:
        correct = ""
        correct += each[::-1]
        print(correct)
        out.write(correct)
    file.close()
    out.close()
    return


file = input("What is the file? \n")
reverse(file)