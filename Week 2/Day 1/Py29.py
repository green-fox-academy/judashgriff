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
print ("Please provide a number!")

num = int(input())
star = "*"
value = 1

while value <= num:
    print (num -1*" " +str(star)* + )