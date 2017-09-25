from tkinter import *
from random import choice
import math
import time


root = Tk()

canvas = Canvas(root, width='420', height='420', highlightthickness=0)
canvas.pack()

def make_hexagon(x, y, size):
    height = math.sqrt(3) / 2 * size
    canvas.create_polygon(x, y,
                          x - size / 2, y + height,
                          x, y + height * 2,
                          x + size, y + height * 2,
                          x + size / 2 + size, y + height,
                          x + size, y,
                          fill=choice(colors), outline='black')


def make_fractal(x, y, size):
    time.sleep(0.00000001)
    canvas.update()
    if size < 2:
        return
    else: 
        height = math.sqrt(3) / 2 * size
        make_hexagon(x, y, size)

        make_fractal(x, y, size / 3)
        make_fractal(x - size / 3, y + height / 3 * 2, size / 3)
        make_fractal(x, y + (height / 3 * 2) * 2, size / 3)

        make_fractal(x + size / 3 * 2, y + height / 3 * 4, size / 3)
        make_fractal(x + size / 2 * 2, y + height / 3 * 2, size / 3)
        make_fractal(x + size / 3 * 2, y, size / 3)


colors = ["black", "white", "whitesmoke", "dimgray", "lightgray", "green", "blue", "gray", "red", "tomato",
          "orange", "tan", "bisque", "darkorange", "lime", "teal", "cyan", "orchid", "lightpink", "brown", "peru", "olive", 
          "darkkhaki", "navy", "crimson", "skyblue", "gold", "magenta", "hotpink", "palevioletred"]

x = 110
y = 10
size = 200

make_fractal(x, y, size)


root.mainloop()