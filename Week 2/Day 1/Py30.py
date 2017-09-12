# Write a program that reads a number from the standard input, then draws a
# diamond like this:
#
#
#    *
#   ***
#  *****
# *******
#  *****
#   ***
#    *
#
# The diamond should have as many lines as the number was

num = int(input("Please enter a number!"))

star = "*"
value = 1
half = num//2

while half >= 1 and num%2==1:
    print (space * " " + value * star)
    value +=2
    space -= 1
while half < num//2+1 and num%2==1:
    print (half * " " + value * star)
    value -=2
    half += 1

while half >= 2 and num%2==0:
    print (half * " " + (value * star))
    value +=2
    half -= 1

if num % 2 == 0:
    value -= 1
else:
    value -=2

while half <= num//2 and num%2==0:
    print (half * " " + value * star)
    value -=2
    half += 1 
    
'''
number = int(input("Give me a number: "))

if number % 2 == 0:
    half = number / 2
else:
    half = number // 2 + 1

i = 1

while i <= half:
    print(" " * (number - i) + "*" * (2 * i - 1))
    i += 1

if number % 2 == 0:
    i -= 1
else:
    i -= 2

while i >= 1:
    print(" " * (number - i) + "*" * (2 * i - 1))
    i -= 1
'''