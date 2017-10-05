from random import randint, choice

class Entity:
    def __init__(self, x, y, image):
        self.position_x = x
        self.position_y = y
        self.image = image
        self.unit_id = None
        self.alive = True

    def move(self, direction):
        if direction == "Up":
            self.position_y -= 1
        elif direction == "Down":
            self.position_y += 1
        elif direction == "Left":
            self.position_x -= 1
        elif direction == "Right":
            self.position_x += 1

    def dice(self):
        return randint(1, 6)

    def random_move(self):
        moves = ["Up", "Down", "Left", "Right"]
        return choice(moves)

class Hero(Entity):
    def __init__(self, x, y, image):
        super().__init__(x, y, image)

    def stats(self):
        self.hero_stats = {
            "experience": 0,
            "level": 1,
            "health":  20 + 3 * self.dice(),
            "defense": 2 * self.dice(),
            "damage": 5 + self.dice()
        }
        return self.hero_stats
        
    
class Skeleton(Entity):
    def __init__(self, x, y, image):
        super().__init__(x, y, image)
        
    def stats(self):
        level = 1
        self.bones = {
            "image": "skeleton",            
            "level": 1,
            "health":  2 * level * self.dice(),
            "defense": (level / 2 * self.dice()) // 1,
            "damage": level * self.dice()
        }
        return self.bones


class Boss(Entity):
    def __init__(self, x, y, image):
        super().__init__(x, y, image)

    def stats(self):
        level = 1
        self.warlock = {
            "image": "boss",
            "level": 1,
            "health":  2 * level * self.dice() + self.dice(),
            "defense": (level / 2 * self.dice() + self.dice() / 2) // 1,
            "damage": level * self.dice() + level
        }
        return self.warlock
