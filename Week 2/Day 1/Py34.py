# Write a program that asks for a number.
# It would ask this many times to enter an integer,
# if all the integers are entered, it should print the sum and average of these
# integers like:
#
# Sum: 22, Average: 4.4

num1 = int(input("Please, provide a number!"))
num2 = int(input("Please, provide an additional number!"))
num3 = int(input("Please, provide an additional number!"))
num4 = int(input("Please, provide an additional number!"))
num5 = int(input("Please, provide an additional number!"))

summary = num1+num2+num3+num4+num5
average = summary / 5
print ("The sum of them is: " + str(summary) + "  The average is: " + str(average))