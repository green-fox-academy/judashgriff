from random import randint

class Pirate(object):
    def __init__(self, name):
        self.name = name
        self.how_much_rum = 0
        self.alive = True


    def drink_some_rum(self):
        if self.alive == False:
            Coco.when_dead()
        else:
            self.how_much_rum += 1
            Coco.when_drinking(self)
            if self.how_much_rum > 7:
                self.knocked_out()
                

    def hows_it_going_mate(self):
        if self.alive == False:
            Coco.when_dead()
        elif self.how_much_rum < 5:
            print("Pour me anudder!")
        elif self.how_much_rum >= 5:
            print("Arghh, I'ma Pirate. How d'ya d'ink its goin?")
            self.knocked_out()
        elif self.how_much_rum > 7:
            self.knocked_out()


    def knocked_out(self):
        Coco.when_knocked_out(pirate)
        self.how_much_rum = 0


    def die(self):
        self.alive = False


    def brawl(self, pirate):
        if self.alive == False or pirate.alive == False:
            Coco.figth_the_dead()
        else:
            Coco.brawl(self, pirate)
            first_outcome = self.dice_check()
            second_outcome = pirate.dice_check()
            if first_outcome and second_outcome == 3:
                pirate.die()
                self.die()
                print("They cut each others guts. Now they're both bled out and dead.")
            elif first_outcome == 3:
                pirate.die()
                Coco.fight_till_death(pirate)
            elif second_outcome == 3:
                self.die()
                Coco.fight_till_death(self)
            else:
                print("No-one has died in the fight today. They both go and drink some rum instead.")
                pirate.drink_some_rum()
                self.drink_some_rum()

    
    def dice_check(self):
        return randint(1, 3)



class Parrot(object):
    def __init__(self, name):
        self.name = name


    def when_dead(self):
        print("He's dead - said " + str(self.name) + " the parrot.")

    def when_drinking(self, pirate):
        print(str(pirate.name) + " had " + str(pirate.how_much_rum) + " rum - said " + str(self.name) + " the parrot.")
        return

    def when_knocked_out(self, pirate):
        print(str(pirate.name) + " passes out from too much rum. The lad's gonna sleep awhile... - said " + str(self.name) + " the parrot.")

    def figth_the_dead(self):
        print("You can't fight the bloody dead! - said " + str(self.name) + " the parrot.")

    def brawl(pirate1, pirate2):
        print(str(pirate1.name) + " and " + str(pirate2.name) + " are in a damn knife-fight! They gonna bloody curve each other up! - said "
              + str(self.name) + " the parrot.")

    def fight_till_death(pirate):
        print(str(pirate.name) + " is dead. He will cause no trouble on the ship anymore. - said " + str(self.name) + " the parrot.")


Jack = Pirate('Jack')
Bill = Pirate('Bill')
Larry = Pirate('Larry')
Coco = Parrot('Coco')


Larry.drink_some_rum()
Larry.drink_some_rum()
Larry.drink_some_rum()
Larry.drink_some_rum()
Bill.brawl(Larry)
Larry.hows_it_going_mate()

