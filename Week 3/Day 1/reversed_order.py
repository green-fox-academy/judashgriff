# Create a method that decrypts reversed-order.txt

def reverse(file):
    f = open(file, "r")
    out = open("ordered2.txt", "w")
    lines = f.readlines()
    lines = lines[::-1]
    lines = "".join(lines)
    print(lines)
    out.write(lines)
    f.close()
    out.close()
    return


file = input("What is the file? \n")
reverse(file)