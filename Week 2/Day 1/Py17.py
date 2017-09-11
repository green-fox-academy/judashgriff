# Write a program that asks for 5 integers in a row,
# then it should print the sum and the average of these numbers like:
#
# Sum: 22, Average: 4.4
print ("Please provide 5 numbers after each!")
num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = int(input())
num5 = int(input())

num = (num1+num2+num3+num4+num5)
average = ((num1+num2+num3+num4+num5)/5)

print ("The total of the numbers are " + str(num) + ".")
print ("The average of the numbers are " + str(average) + ".")