# Write a program that reads a number from the standard input, then draws a
# square like this:
#
#
# %%%%%
# %   %
# %   %
# %   %
# %   %
# %%%%%
#
# The square should have as many lines as the number was

num = int(input("Please provide a number!"))

envelope = num * "%"
between = ("%" + (num-2)* " " +"%")

if num <= 2:
    for i in range(num):
        print (envelope)
    
elif num > 2:
    print (envelope)
    for i in range(num-2):
        print (between)
    print (envelope)