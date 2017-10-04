from random import randint

class Entity:
    def __init__(self, x, y, image):
        self.position_x = x
        self.position_y = y
        self.image = image
        self.unit_id = None

    def move(self, direction):
        if direction == "up":
            self.position_y -= 1
        elif direction == "down":
            self.position_y += 1
        elif direction == "left":
            self.position_x -= 1
        elif direction == "right":
            self.position_x += 1

    def dice(self):
        return randint(1, 6)

class Hero(Entity):
    def __init__(self, x, y, image):
        super().__init__(x, y, image)

    def hero_attributes(self):
        self.hero_stats = {
            "experience": 0,
            "level": 1,
            "health":  20 + 3 * self.dice(),
            "defense": 2 * self.dice(),
            "damage": 5 + self.dice()
        }
        return self.hero_stats
        
    
class Monster(Entity):
    def __init__(self, x, y, image):
        super().__init__(x, y, image)

    def skeleton(self):
        self.skeleton = {
            "level": 1,
            "health":  2 * self.skeleton["level"] * self.dice,
            "defense": (self.skeleton["level"] / 2 * self.dice) // 1,
            "damage": self.skeleton["level"] * self.dice
        }
        return self.skeleton
        

    def boss(self):
        self.boss = {
            "level": 1,
            "health":  2 * self.boss["level"] * self.dice + self.dice,
            "defense": (self.boss["level"] / 2 * self.dice + self.dice / 2) // 1,
            "damage": self.boss["level"] * self.dice + self.boss["level"]
        }
        return self.boss