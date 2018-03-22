from map import Map
from view import View
from entity import Entity, Hero, Boss, Skeleton
from random import randint
import sys


class Game:
    def __init__(self):
        # self.game_status()
        self.my_map = Map()
        self.my_view = View(self.my_map.map1)
        self.combat = Fight_engine()
        self.my_view.root.bind("<KeyPress>", self.on_key_press)
        self.creatures = [Boss(0, 7, "boss")]
        self.get_random_skeletons()
        self.get_units()
        self.hero = Hero(0, 0, "hero-down")
        self.hero.unit_id  = self.my_view.draw_game_object(0, 0, "hero-down")
        self.movement_count = 0
        self.delete_dead_creature()
        self.hud()
        self.my_view.start()

    def get_random_skeletons(self):
        skeletons = randint(1, 6)
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
                    self.creatures.append(Skeleton(x, y, "skeleton"))
                    skeletons -= 1

    def get_units(self):
        for unit in self.creatures:
            unit.unit_id = self.my_view.draw_game_object(unit.position_x, 
                                                    unit.position_y, 
                                                    unit.image)

    def on_key_press(self, e):
        if not self.hero.enemy_to_kill:
            if e.keysym == "Up" or  e.keysym == "Down" or e.keysym == "Left" or e.keysym == "Right":
                self.move_hero(e.keysym)
                self.check_if_meeting()
        elif self.hero.enemy_to_kill:
            if e.keysym == "space":
                self.check_if_meeting()

    def move_hero(self, direction):
        if direction == "Up" or direction == "Down" or direction == "Left" or direction == "Right":
            self.move_counter()
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

    def move_counter(self):
        self.movement_count += 1
        if self.movement_count == 2:
            for creature in self.creatures:
                direction = creature.random_move()
                self.monster_move_check(creature, direction)
            self.movement_count = 0

    def monster_move_check(self, creature, direction):
        if_valid = self.check_direction_validity(direction, creature)
        if if_valid:
            self.move_enemies(creature, direction)

    def move_enemies(self, creature, direction):
        self.my_view.canvas.itemconfigure(creature.unit_id, image=self.my_view.images[creature.image])
        if direction == "Up":
            self.my_view.canvas.move(creature.unit_id, 0, -72)
            creature.move(direction)
        elif direction == "Down":
            self.my_view.canvas.move(creature.unit_id, 0, 72)
            creature.move(direction)
        elif direction == "Left":
            self.my_view.canvas.move(creature.unit_id, -72, 0)
            creature.move(direction)
        elif direction == "Right":
            self.my_view.canvas.move(creature.unit_id, 72, 0)
            creature.move(direction)

        
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

    def check_if_meeting(self):
        for creature in self.creatures:
            if self.hero.position_x == creature.position_x and self.hero.position_y == creature.position_y:
                self.hero.enemy_to_kill = creature
                self.my_view.battle_hud(creature.stats())
                self.combat.battle_on(self.hero, creature, self.my_view, self.hero.enemy_to_kill)
            elif self.hero.enemy_to_kill:
                self.my_view.canvas.delete(self.my_view.battle_hud_id)
                self.hero.enemy_to_kill = None

    def delete_dead_creature(self):
        self.my_view.canvas.delete(self.combat.dead_creature)
        self.my_view.root.after(100, self.delete_dead_creature)

    def hud(self):
        self.my_view.hud(self.hero.stats())

    def game_status(self):

        if self.is_going == False:
            pass 
            # Game Over

class Fight_engine():
    def __init__(self):
        self.dead_creature = None

    def battle_on(self, hero, enemy, my_view, status):
        if hero.alive == True and enemy.alive == True:
            self.strike(hero, enemy)
            hero_stats = hero.stats()
            if hero_stats["health"] < 1:
                self.game_over(my_view, status)
    
    def strike(self, attacker, defender):
        attacker_stats = attacker.stats()
        defender_stats = defender.stats()
        attacker_strike = attacker_stats["damage"] + 2 * randint(1, 6)
        if attacker_strike > defender_stats["defense"]:
            defender_stats["health"] -= attacker_strike - defender_stats["defense"]
            if defender_stats["health"] < 1:
                defender.alive = False
                self.dead_creature = defender.unit_id
            else:
                self.strike(defender, attacker)


    def game_over(self, my_view, status):
        status = my_view.game_over()
        sys.exit(0)


game = Game()