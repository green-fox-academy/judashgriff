# Write a program that stores a number, and the user has to figure it out.
# The user can input guesses, after each guess the program would tell one
# of the following:
#
# The stored number is higher
# The stried number is lower
# You found the number: 8

num = 8

guess = int(input("Please guess a number from 0-10!"))

if guess == num:
    print ("Yayy, You got it!")
elif guess > num:
    print ("The stried number is lower!")
elif guess < num:
    print ("The stored number is higher")