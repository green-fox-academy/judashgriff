from random import randint

class Dice(object):

    def __init__(self):
        self.dice = [0, 0, 0, 0, 0, 0]

    def roll(self):
        for i in range(len(self.dice)):
            self.dice[i] = randint(1,6)
        return self.dice

    def get_current(self, index=None):
        if index != None:
            return self.dice[index]
        else:
            return self.dice

    def reroll(self, index=None):
        if index != None:
            self.dice[index] = randint(1,6)
        else:
            self.roll()

    # def see_if_six(self):
    #     for i in get_current:
    #         self.dice[i] == 6


my_dice = Dice()
my_dice.roll()
print(my_dice.get_current)

def dice_to_six(my_dice):
    for i in range(len(my_dice.dice)):
        while my_dice.get_current(i) != 6:
            my_dice.reroll(i)


dice_to_six(my_dice)
print(my_dice.dice)