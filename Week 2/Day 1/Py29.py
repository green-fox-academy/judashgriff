# Write a program that reads a number from the standard input, then draws a
# pyramid like this:
#
#
#    *
#   ***
#  *****
# *******
#
# The pyramid should have as many lines as the number was
num = int(input("Please provide a number!"))

star = "*"
value = 1
space = num

while space > 0:
    print ((space-1) * " " + (0 + value) * star)
    value +=2
    space -= 1