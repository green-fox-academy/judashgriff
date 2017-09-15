# Write a program where the program chooses a number between 1 and 100. The player is then asked to enter a guess. If the player guesses wrong, then the program gives feedback and ask to enter an other guess until the guess is correct.

# Make the range customizable (ask for it before starting the guessing).
# You can add lives. (optional)
# Example

# I've the number between 1-100. You have 5 lives.

# 20
# Too high. You have 4 lives left.

# 10
# Too low. You have 3 lives left.

# 15
# Congratulations. You won!
from random import randint


number = randint(0, int(input("What will be the scope for the game? 0 to... ? Enter a maximum!: ")))


def guessing_game(number):
    lives = 5
    for trying in range(lives):
        guess = int(input("Guess a number! "))
        if guess == number:
            print("Congratulation! You guessed correct!")
            return
        elif guess < number:
            lives -= 1
            print("Nope, this is too little! You have " + str(lives) + " lives left!")
        elif guess > number: 
            lives -= 1
            print("Nope, this is too much! You have " + str(lives) + " lives left!")
    print("You have no more lives left! You lose!")
    if lives == 0: 
        return

guessing_game(number)