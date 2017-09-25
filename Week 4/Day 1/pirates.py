class Pirates(object):
    def __init__(self, name):
        self.name = name
        self.how_much_rum = 0


    def drink_some_rum(self):
        self.how_much_rum += 1
        print(self.name + " had " + self.how_much_rum + " rum.")

    def hows_it_going_mate():
        if self.drink_some_rum < 5:
            print("Pour me anudder!")
        elif self.drink_some_rum >= 5:
            print("Arghh, I'ma Pirate. How d'ya d'ink its goin?")

    # def die():


Jack = Pirates('Jack')
Bill = Pirates('Bill')
Larry = Pirates('Larry')

print(Jack.hows_it_going_mate, Jack.drink_some_rum, Jack.hows_it_going_mate)