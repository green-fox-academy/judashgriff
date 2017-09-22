from tkinter import *
import math
import time

root = Tk()

canvas = Canvas(root, width='400', height='400', bd=0, highlightthickness=0)
canvas.pack()

def draw_beehive_thing(x,y,width):
    height = math.sqrt(3) / 2 * width
    canvas.create_polygon(x, y, x + width / 2, y - height,
                          x + width * 1.5, y - height, 
                          x + width * 2,  y,
                          x + width * 1.5, y + height,
                          x + width / 2, y + height,
                          fill = 'yellow', outline='black')


def draw_fractal(x,y,width):
    time.sleep(0.001)
    canvas.update()
    if width < 5:
        return
    else:
        height = math.sqrt(3) / 2 * width
        draw_beehive_thing(x, y, width)
        draw_fractal(x + width / 4, y - height / 2, width/2)
        draw_fractal(x + width, y, width / 2)
        draw_fractal(x + width / 4, y + height / 2, width/2)


x = 10
y = 200
width = 150

draw_fractal(x, y, width,)


root.mainloop()
