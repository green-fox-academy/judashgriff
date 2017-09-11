# Write a program that asks for two numbers and prints the bigger one

print ("Please, provide two numbers after each.")
num1 = int(input())
num2 = int(input())

if num1>num2:
    print ("The bigger is obviously number " + str(num1))
if num1<num2:
    print ("The bigger is obviously number " + str(num2))