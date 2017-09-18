# Create a method that decrypts the duplicated-chars.txt

def decrypt(file_name):
    file = open(file_name, "r")
    out = open("output.txt", "w")
    for each in file:
        correct = ""
        correct += each[::2]
        out.write(correct)
    file.close()
    out.close()
    return


file = input("What is the file? \n")
decrypt(file)