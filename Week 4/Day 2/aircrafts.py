from random import choice

class Aircraft(object):
    def __init__(self):
        self.base_ammo = 0

    def flight(self):
        if self.current_ammo <= 0:
            damage = self.damage_counter()
            print("The aircraft is out of ammo. It will return to refuel. It caused " + str(damage) + " damage.")

    def damage_counter(self):
        damage = self.current_ammo * self.base_damage
        return damage

    def refill(self, value):
        ammo_stock = value
        while ammo_stock > 0 and self.current_ammo != self.max_ammo:
            ammo_stock -= 1
            self.current_ammo += 1
        print("The " + str(self.name) + " has refueled and her weaponry is loaded. She has " 
              + str(self.current_ammo) + " ammo. The ammo stock has " + str(ammo_stock) + " units of ammunition remaining.")
        
    def getStatus(self):
        print("Type: " + self.__class__.__name__ + ", Ammo: " + str(self.current_ammo) + ", Base damage: " 
              + str(self.base_damage) + ", ALL damage: " + str(self.max_ammo * self.base_damage))



class F16(Aircraft):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.name = name
        self.max_ammo = 8
        self.base_damage = 30

    current_ammo = 0



class F35(Aircraft):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.max_ammo = 8
        self.base_damage = 30

    current_ammo = 0



class Carrier(object):
    def __init__(self, name, ammo, health):
        self.name = name
        self.aircrafts = []
        self.store_ammo = ammo
        self.carrier_health = health
        self.f16 = F16()
        self.f35 = F35()

    def add_aircraft(self, type_of):
        if type_of == F16 or type_of == F35:
            self.aircrafts.append(type_of)
        for aircraft in self.aircrafts:
            print(aircraft)

    def fill(self):
        for aircraft in self.aircrafts:
            if aircraft == F16:
                aircraft = F16(choice(aircraft_names))
            elif aircraft == F35:
                aircraft = F35(choice(aircraft_names))



aircraft_names = ['Airabonita', 'Airacobra', 'Airacomet', 'Apache', 'Argus', 
                  'Ascender', 'Avenger', 'Baltimore', 'Bat', 'Bearcat', 'Bermuda', 
                  'Black Bullet', 'Black Widow', 'Bobcat', 'Bolo', 'Boston', 
                  'Buccaneer', 'Buffalo', 'Canso', 'Corsair']


freedom = F16('Freedom')
serenity = F35('Serenity')

freedom.flight()
freedom.refill(30)

freedom.getStatus()

justice = Carrier('Justice', 600, 4000)

justice.add_aircraft(F16)
justice.add_aircraft(F16)
justice.add_aircraft(F35)
justice.add_aircraft(F35)