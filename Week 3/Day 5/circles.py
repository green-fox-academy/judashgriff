from tkinter import *
import math
import time

root = Tk()

canvas = Canvas(root, width='420', height='420', bd=0, highlightthickness=0)
canvas.pack()

def circle(x,y,size):
    canvas.create_oval(x - size / 2, y - size / 2, x + size / 2, y + size / 2, fill = '', outline='black')


def get_triangle_side(height):
    return math.sqrt(4*height**2/3)


def draw_fractal(x,y,size):
    time.sleep(0.1)
    canvas.update()
    if size < 20:
        return
    else:
        circle(x, y, size)
        triangle_height = size * 0.75
        triangle_side = get_triangle_side(triangle_height)
        draw_fractal(x, y - size / 4, size / 2)
        draw_fractal(x - triangle_side / 4, y + size / 8, size / 2)
        draw_fractal(x + triangle_side / 4, y + size / 8 , size / 2)


x = 210
y = 210
size = 400

draw_fractal(x, y, size)


root.mainloop()
