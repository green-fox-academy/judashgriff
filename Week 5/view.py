from tkinter import *
from map import Map
from entity import Entity, Hero, Monster
import time

class View:
    def __init__(self):
        self.my_map = Map()
        self.size = 720
        self.zero_point = 36
        self.hud = 150
        self.root = Tk()
        self.root.configure(background ='black')
        self.canvas = Canvas(self.root, width=self.size+self.hud, height=self.size, bg="teal", bd=0)
        self.canvas.pack(expand=YES, fill=BOTH)
        self.rect = None
        self.floor = PhotoImage(file='floor.png')
        self.wall = PhotoImage(file='wall.png')
        self.create_map(self.zero_point+self.hud, self.zero_point, 72)
        self.draw_hero(self.zero_point+self.hud, self.zero_point, 72)
        self.root.bind("<KeyPress>", self.on_key_press)
        self.canvas.focus_set()
        # self.fill_hud()
        self.root.mainloop()

    def create_map(self, x, y, size):
        for row in range(10):
            for column in range(10):
                if self.my_map.map1[column][row] == 0:
                    self.rect = self.canvas.create_image(x+size*row, y+size*column, image = self.wall)
                if self.my_map.map1[column][row] == 1:
                    self.rect = self.canvas.create_image(x+size*row, y+size*column, image = self.floor)

    def draw_hero(self, x, y, size):
        self.h = PhotoImage(file='hero-down.png')
        self.hero = self.canvas.create_image(x, y, image = self.h)

    def hero_shape(self, direction):
        if direction == 'Down':
            self.h = PhotoImage(file='hero-down.png')
            return self.h
        elif direction ==  'Up':
            self.h = PhotoImage(file='hero-up.png')
            return self.h
        elif direction ==  'Right':        
            self.h = PhotoImage(file='hero-right.png')
            return self.h
        elif direction ==  'Left':
            self.h = PhotoImage(file='hero-left.png')
            return self.h
        
    def move(self, x, y):
        
        for i in range(20):
            time.sleep(0.0001)
            self.canvas.update()
            self.canvas.move(self.hero, x * 72 / 20, y * 72 / 20)

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



    # def fill_hud(self):
    #     pass

myView = View()


