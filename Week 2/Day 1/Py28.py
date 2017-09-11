# Write a program that reads a number from the standard input, then draws a
# triangle like this:
#
# *
# **
# ***
# ****
#
# The triangle should have as many lines as the number was

print ("Please provide a number.")

number = int(input())

star ="*"
ax = 1
while ax <= number:
    print (str(star)*ax)
    ax += 1