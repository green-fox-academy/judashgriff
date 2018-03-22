from tkinter import *
import time
import entity

class View:
    def __init__(self, my_map):
        self.my_map = my_map
        self.create_canvas()
        self.images = {"wall": PhotoImage(file='./wall.png'),
                       "floor": PhotoImage(file='./floor.png'),
                       "hero-down": PhotoImage(file='./hero-down.png'),
                       "hero-up": PhotoImage(file='./hero-up.png'),
                       "hero-left": PhotoImage(file='./hero-left.png'),
                       "hero-right": PhotoImage(file='./hero-right.png'),
                       "skeleton": PhotoImage(file='./skeleton.png'),
                       "boss": PhotoImage(file='./boss.png')
                       }
        self.create_map()
        self.canvas.focus_set()
        self.battle_hud_id = None
       
    def start(self):
        self.root.mainloop()
    
    def create_canvas(self):
        self.root = Tk()
        self.root.configure(background ='black')
        self.canvas = Canvas(self.root, width=920, height=720, bg="teal", bd=0, highlightthickness=0)
        self.canvas.pack(expand=YES, fill=BOTH)

    def draw_game_object(self, x, y, image):
        size = 72
        x_offset = 236
        y_offset = 36
        return self.canvas.create_image(x * size + x_offset, y * size + y_offset, image = self.images[image])
        
    def create_map(self):
        for y in range(10):
            for x in range(10):
                if self.my_map[y][x] == 0:
                    self.draw_game_object(x, y, image="wall")
                if self.my_map[y][x] == 1:
                    self.draw_game_object(x, y, image="floor")

    def hud(self, hero_stats):
        floor = 1
        self.canvas.create_text(10, 10, font="Times 14 bold", fill="white", text="Floor: " + str(floor) +  "\n\nHero level:  Level " + str(hero_stats["level"]) + "\
                                \nHealth points:  " + str(hero_stats["health"]) + "\
                                \nDefense point:  " + str(hero_stats["defense"]) + "\
                                \nStrike point:  " + str(hero_stats["damage"]), anchor=NW)

    def battle_hud(self, enemy):
        self.battle_hud_id = self.canvas.create_text(10, 165, font="Times 14 bold", fill="white", text="You have entered to a \
                                \nbattle with a " + str(enemy["image"]) + "!\
                                \nPrepare to defend\
                                \nyour life! \
                                \nPress space to attack!\n\
                                \nEnemy stats:\n\
                                \nLife: " + str(enemy["health"]) + "\
                                \nDefense point:  " + str(enemy["defense"]) + "\
                                \nStrike point:  " + str(enemy["damage"]), anchor=NW)

    def game_over(self):
        self.canvas.create_text(560, 360, font="Times 60 bold", text="You are dead!\
                                \nGame Over\
                                \nPress \"x\" to exit", anchor=CENTER)
        return "game over"