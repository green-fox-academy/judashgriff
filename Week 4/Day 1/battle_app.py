from random import randint
from pirates import Ship

class To_battle(object):
    def __init__(self):
        self.ship1 = Ship()
        self.ship2 = Ship()
        self.ship1.battle()
        self.ship2.battle()
        self.fight_battle()
    
    def fight_battle(self):
        if self.ship1.score > self.ship2.score:
            self.update_after_battle(self.ship1, self.ship2)
        else:
            self.update_after_battle(self.ship2, self.ship1)

    def deaths(self, loser):
        deaths = randint(1, loser.crew)
        return deaths

    def update_after_battle(self, winner, loser):
        deaths = self.deaths(loser)
        loser.crew -= deaths
        print(str(winner.ship_name) + " has won the battle with Captain " 
        + winner.captain_name + "! Captain " + loser.captain_name + " has lost " 
        + str(deaths) + " men! The winners drink their well deserved rum! ")

indian_ocean = To_battle()