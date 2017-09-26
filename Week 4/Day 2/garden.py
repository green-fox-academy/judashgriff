class Garden(object):
    def __init__(self, plants):
        self.garden = plants

    def all_in_garden(self):
        for plant in self.garden:
            print("There is a " + str(plant.plant_name) + " in the garden.")

    def give_water(self, amount):
        thirsty = []
        for i in self.garden:
            if i.had_enough == False:
                thirsty.append(i)
        each_water = amount / len(thirsty)
        for i in thirsty:
            i.take_water(each_water)
            i.water_got += each_water
        self.printer()
        
    def printer(self):
        for plant in self.garden:
            if plant.had_enough == False:
                print("The " + str(plant.plant_name) + " needs water.")
                print("Water level: " + str(plant.water_taken_in) + ". Water required: " + str(plant.water_needed_amount) + ".")
            if plant.had_enough == True:
                print("The " + str(plant.plant_name) + " is fine.")
                print("Water level: " + str(plant.water_taken_in) + ". Water required: " + str(plant.water_needed_amount) + ".")
            


class Plant(object):

    def take_water(self, each_water):
        self.water_got += each_water
        self.water_conversion()
    
    water_got = 0
    water_taken_in = 0
    had_enough = False

    def drink_water(self):
        if self.water_taken_in >= self.water_needed_amount:
            self.had_enough = True



class Flower(Plant):
    def __init__(self, name):
        super().__init__()
        self.plant_name = name
        
    water_needed_amount = 5

    def water_conversion(self):
        drank_water = self.water_got * 0.75
        self.water_taken_in += drank_water
        self.drink_water()



class Tree(Plant):
    def __init__(self, name):
        super().__init__()
        self.plant_name = name

    water_needed_amount = 10

    def water_conversion(self):
        drank_water = self.water_got * 0.4
        self.water_taken_in += drank_water
        self.drink_water()



def add_plants():
    plants = []
    plants.append(Flower('yellow Flower'))
    plants.append(Flower('blue Flower'))
    plants.append(Tree('purple Tree'))
    plants.append(Tree('orange Tree'))
    return plants


plants = add_plants()

garden = Garden(plants)
garden.all_in_garden()