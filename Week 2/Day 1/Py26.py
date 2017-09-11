# Create a program that asks for two numbers
# If the second number is not bigger than the first one it should print:
# "The second number should be bigger"
#
# If it is bigger it should count from the first number to the second by one
# 
# example:
#
# first number: 3, second number: 6, should print:
#
# 3
# 4
# 5

print ("Please provide two numbers!")

num1 = int(input())
num2 = int(input())

if num2 <= num1:
    print ("The secont number should be bigger")

if num1 < num2:
    while num2 > num1:
        print (num1)
        num1 += 1