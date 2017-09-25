from tkinter import *
import time
from random import choice, randint
root = Tk()

canvas = Canvas(root, width=420, height=420, bd=0, highlightthickness=0)
canvas.pack()

def triangle(x,y,size):
    canvas.create_polygon(x, y, x + size, y, x + size / 2, y + size, fill=choice(colors), outline='black')


def draw_fractal(x,y,size):
    time.sleep(0.00001)
    canvas.update()
    # animation.update()
    if size < 5:
    #     for x in range(0, 1):
    #         canvas.move(1, 3, 0)
    #         animation.update()
    #     for x in range(0, 1):
    #         canvas.move(1, -3, 0)
    #         animation.update()
    #     for x in range(0, 1):
    #         canvas.move(1, 0, 3)
    #         animation.update()
    #     for x in range(0, 1):
    #         canvas.move(1, 0, -3)
    #         animation.update()
        return
    else:
        triangle(x, y, size)
        draw_fractal(x, y, size / 2)
        draw_fractal(x + size / 2, y, size / 2)
        draw_fractal(x + size / 4, y + size / 2 , size / 2)



colors = ["black", "white", "whitesmoke", "dimgray", "lightgray", "green", "blue", "gray", "red", "tomato",
          "orange", "tan", "bisque", "darkorange", "lime", "teal", "cyan", "orchid", "lightpink", "brown", "peru", "olive", 
          "darkkhaki", "navy", "crimson", "skyblue", "gold", "magenta", "hotpink", "palevioletred"]


random_num = randint(0, 100)

x = 10
y = 10
size = 400 - random_num

draw_fractal(x, y, size)


root.mainloop()
