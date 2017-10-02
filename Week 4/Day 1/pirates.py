from random import randint, choice

class Pirate(object):
    def __init__(self, name):
        self.name = name
        self.how_much_rum = 0
        self.alive = True
        self.awake = True

    def drink_some_rum(self):
        if self.alive == False:
            coco.when_dead()
        else:
            self.how_much_rum += 1
            print(str(self.name) + " had " + str(self.how_much_rum) + " rum.")
            if self.how_much_rum > 7:
                self.knocked_out()

    def hows_it_going_mate(self):
        if self.alive == False:
            coco.when_dead()
        elif self.how_much_rum < 5:
            print("Pour me anudder!")
        elif self.how_much_rum >= 5:
            print("Arghh, I'ma Pirate. How d'ya d'ink its goin?")
            self.knocked_out()
        elif self.how_much_rum > 7:
            self.knocked_out()
            if self.awake == False:
                print(str(self.name) + " passes out from too much rum. The lad's gonna sleep awhile.")

    def knocked_out(self):
        self.awake = False
        self.how_much_rum = 0

    def die(self):
        self.alive = False

    def brawl(self, pirate):
        if self.alive == False or pirate.alive == False:
            coco.figth_the_dead()
        else:
            print(str(self.name) + " and " + str(pirate.name) 
                  + " are in a damn knife-fight! They gonna bloody curve each other up!")
            first_outcome = self.dice_check()
            second_outcome = pirate.dice_check()
            if first_outcome and second_outcome == 3:
                pirate.die()
                self.die()
                print("They cut each others guts. Now they're both bled out and dead.")
            elif first_outcome == 3:
                pirate.die()
                print(str(pirate.name) + " is dead. He will cause no trouble on the ship anymore.")
            elif second_outcome == 3:
                self.die()
                print(str(self.name) + " is dead. He will cause no trouble on the ship anymore.")
            else:
                print("No-one has died in the fight today. They both go and drink some rum instead.")
                pirate.drink_some_rum()
                self.drink_some_rum()

    def dice_check(self):
        return randint(1, 3)


class Captain(Pirate):
    def __init__(self, name):
        super().__init__(name)
        self.rum = 0


    def how_s_d_captn(self):
        self.get_some_rum()
        if self.alive == False:
            print("The captain is dead! Run for your lives!\n")
        elif self.awake == False:
            print("The captain had too much rum! He's licking up the deck now!\n")
        else:
            print(str(self.name) + " has all in control. The ship is on course towards a glorious raid!\n")

    def get_some_rum(self):
        return self.is_awake(randint(1, 6))

    def is_awake(self, rum):
        self.rum = rum
        if rum < 5:
            self.awake = False
        return 


class Parrot(object):
    def __init__(self, name):
        self.parrot_name = name

    def when_dead(self):
        print("HE'S DEAD, HE'S DEAAAD!- said " + str(self.parrot_name) + " the parrot.")

    def figth_the_dead(self):
        print("YE CANT FIGHT DY BLAADY DEED! - said " + str(self.parrot_name) + " the parrot.")


class Ship(object):
    def __init__(self):
        self.pirates = Pirate('Pirate'+ str(randint(100, 1000)))
        self.captain_name = self.captain_on_board()
        self.captain = Captain(self.captain_name)
        self.ship_name = self.ships_name()
        self.get_ready()
        self.score = 0

    def get_ready(self):
        self.fill_ship()
        self.captain.how_s_d_captn()

    def fill_ship(self):
        self.crew = self.crew_on_board()
        print(str(self.crew) + " pirates boarded the " + str(self.ship_name) + 
              " with the the lead of captain " + str(self.captain_name) 
              + " ALL PREPARE FOR WAR!")
        return

    def crew_on_board(self):
        return randint(5, 50)

    def captain_on_board(self):
        return choice(self.captains_list)

    def ships_name(self):
        return choice(self.ship_names_list)

    def battle(self):
        self.score = self.crew - self.captain.rum
    

    captains_list = ['Jack Sparrow', 'Will Turner', 'Larry Ole', 'Davy Jones', 'Blackbeard', 'Barbossa']
    ship_names_list = ['The Black Pearl', 'Surprise', 'The Sunken Bottle',
                       'The Empresses Wrath', 'The Horrid Rose', 'The Drunken Executioner']


# jack = Captain('Jack Sparrow')
# bill = Captain('Will Turner')
# larry = Captain('Larry Ole')
# jones = Captain('Davy Jones')
# blackbeard = Captain('Blackbeard')
# barbossa = Captain('Barbossa')
# coco = Parrot('coco')
# ship = Ship()

# jack.brawl(larry)
