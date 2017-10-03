from tkinter import *
# from entity import Entity, Hero, Monster
import time

class View:
    def __init__(self, my_map):
        self.my_map = my_map
        self.create_canvas()
        self.models = {"wall": PhotoImage(file='wall.png'),
                       "floor": PhotoImage(file='floor.png'),
                       "hero-down": PhotoImage(file='hero-down.png'),
                       "hero-up": PhotoImage(file='hero-up.png'),
                       "hero-left": PhotoImage(file='hero-left.png'),
                       "hero-right": PhotoImage(file='hero-right.png'),
                       }
        self.create_map()
        self.root.bind("<KeyPress>", self.on_key_press)
        self.canvas.focus_set()
        # self.fill_hud()
       
    def start(self):
        self.root.mainloop()
    
    def create_canvas(self):
        self.root = Tk()
        self.root.configure(background ='black')
        self.canvas = Canvas(self.root, width=870, height=720, bg="teal", bd=0)
        self.canvas.pack(expand=YES, fill=BOTH)

    def draw_game_object(self, x, y, model):
        size = 72
        x_offset = 186
        y_offset = 36
        return self.canvas.create_image(x * size + x_offset, y * size + y_offset, image = self.models[model])
        
    def create_map(self):
        for y in range(10):
            for x in range(10):
                if self.my_map[x][y] == 0:
                    self.draw_game_object(x, y, model="wall")
                if self.my_map[x][y] == 1:
                    self.draw_game_object(x, y, model="floor")

    def on_key_press(self, e):
        self.coords = self.canvas.coords(self.hero)
        self.facing = self.hero_shape(e.keysym)
        if ( e.keysym == 'Up' ):
            self.hero = self.canvas.create_image(self.coords[0], self.coords[1], image = self.h)
            self.move(0, -1)
        elif( e.keysym == 'Down' ):
            self.hero = self.canvas.create_image(self.coords[0], self.coords[1], image = self.h)
            self.move(0, 1)
        elif ( e.keysym == 'Left' ):
            self.hero = self.canvas.create_image(self.coords[0], self.coords[1], image = self.h)
            self.move(-1, 0)
        elif( e.keysym == 'Right' ):
            self.hero = self.canvas.create_image(self.coords[0], self.coords[1], image = self.h)
            self.move(1, 0)

    # def is_valid_cell(self):


    # def fill_hud(self):
    #     pass