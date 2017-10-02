from random import randint

class Game(object):
    def __init__(self):
        self.number = self.create_number()

    def create_number(self):
        number = randint(1000, 9999)
        return number
        

    def game_state(self):
        playing or finished
        pass


class Guess(Game):
    def __init__(self):
        super().__init__()
        self.guesses = 0
        self.guess_something()

    def guess_something(self):
        beginning = "'LEt\'s play! Guess a nomber from my random generated four digit number!"
        if self.guesses == 0:
            guess_first = (int(beginning + '\n It is ' + str(self.number) + ', but don\'t tell anybody! '))
            self.guesses += 1
        elif self.guesses == 0 < self.guesses < 5:
            guess_again = (int('Guess again! '))
            self.guesses += 1
        elif self.guesses == 5:
            print('Sorry bro! No more guesses. You lost this time, but try again!')

        