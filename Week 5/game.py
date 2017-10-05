from map import Map
from view import View
from entity import Entity, Hero, Monster
from random import randint


class Game:
    def __init__(self):
        # self.game_status()
        self.my_map = Map()
        self.my_view = View(self.my_map.map1)
        self.my_view.root.bind("<KeyPress>", self.on_key_press)
        self.creatures = [Entity(0, 7, "boss")]
        self.get_random_skeletons()
        self.get_units()
        self.hero = Hero(0, 0, "hero-down")
        self.hero.unit_id  = self.my_view.draw_game_object(0, 0, "hero-down")
        self.enemy = Monster(0, 0, "Skeleton")
        self.hud()
        self.is_going = True
        self.my_view.start()

    def get_random_skeletons(self):
        skeletons = randint(3, 6)
        while skeletons > 0:
            x = randint(1, 9)
            y = randint(1, 9)
            valid = self.my_map.cell_validation(x, y)
            if valid:
                can_insert_skeleton = True
                for creature in self.creatures:
                    if x == creature.position_x and y == creature.position_y:
                        can_insert_skeleton = False
                if can_insert_skeleton:
                    self.creatures.append(Entity(x, y, "skeleton"))
                    skeletons -= 1

    def get_units(self):
        for unit in range(len(self.creatures)):
            unit_id = self.my_view.draw_game_object(self.creatures[unit].position_x, 
                                                    self.creatures[unit].position_y, 
                                                    self.creatures[unit].image)

    def on_key_press(self, e):
        self.move_hero(e.keysym)
        self.move_counter(e.keysym)

    def move_hero(self, direction):
        self.facing = self.my_view.images["hero-" + direction.lower()]
        self.my_view.canvas.itemconfigure(self.hero.unit_id, image=self.facing)
        self.valid = self.check_direction_validity(direction, self.hero)
        if direction == "Up" and self.valid:
            self.my_view.canvas.move(self.hero.unit_id, 0, -72)
            self.hero.move(direction)
        elif direction == "Down" and self.valid:
            self.my_view.canvas.move(self.hero.unit_id, 0, 72)
            self.hero.move(direction)
        elif direction == "Left" and self.valid:
            self.my_view.canvas.move(self.hero.unit_id, -72, 0)
            self.hero.move(direction)
        elif direction == "Right" and self.valid:
            self.my_view.canvas.move(self.hero.unit_id, 72, 0)
            self.hero.move(direction)

    moves = 0

    def move_counter(self, move):
        if move:
            self.moves += 1
            print(self.moves)
            if self.moves == 2:
                movement = self.enemy.random_move()
                self.moves = 0
                self.move_monsters(movement)

    def move_monsters(self, movement):
        if_valid = self.check_direction_validity(movement, self.enemy)
        if if_valid == False:
            movement = self.enemy.random_move()
            self.move_monsters(movement)
        else:
            self.enemy.move(movement)
        
    def check_direction_validity(self, direction, guy):
        if direction == "Up":
            self.validity = self.my_map.cell_validation(guy.position_x, guy.position_y - 1)
        elif direction == "Down":
            self.validity = self.my_map.cell_validation(guy.position_x, guy.position_y + 1)
        elif direction == "Left":
            self.validity = self.my_map.cell_validation(guy.position_x - 1, guy.position_y)
        elif direction == "Right":
            self.validity = self.my_map.cell_validation(guy.position_x + 1, guy.position_y)
        return self.validity

    def hud(self):
        self.my_view.hud(self.hero.hero_attributes())

    # def game_status(self):
    #     if self.is_going == False:
    #         pass 
    #         # Game Over

class Fight_engine:
    def __init__(self):
        self.hero_stats


game = Game()

