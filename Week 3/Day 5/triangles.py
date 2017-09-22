from tkinter import *
import math
import time

root = Tk()

canvas = Canvas(root, width='420', height='420', bd=0, highlightthickness=0)
canvas.pack()

def circle(x,y,size):
    canvas.create_oval(x, y, x + size, y +size, fill = '', outline='black')


def draw_fractal(x,y,size):
    time.sleep(0.001)
    canvas.update()
    if size < 20:
        return
    else:
        circle(x, y, size)
        draw_fractal(x + size / 4, y, size / 2)
        draw_fractal(x, y + size / 3, size / 2)
        draw_fractal(x + size / 2, y + size / 3 , size / 2)


x = 10
y = 10
size = 400

draw_fractal(x, y, size)


root.mainloop()
