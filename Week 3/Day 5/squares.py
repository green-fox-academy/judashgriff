from tkinter import *
from random import choice


root = Tk()

canvas = Canvas(root, width='420', height='420', highlightthickness='0')
canvas.pack()

def make_squares(x, y, size, width):
    canvas.create_rectangle(x - size /2, y - size / 2, x + size /2, y + size / 2, width=width, fill='', outline=choice(colors))


colors = ["black", "white", "whitesmoke", "dimgray", "lightgray", "green", "blue", "gray", "red", "tomato",
          "orange", "tan", "bisque", "darkorange", "lime", "teal", "cyan", "orchid", "lightpink", "brown", "peru", "olive", 
          "darkkhaki", "navy", "crimson", "skyblue", "gold", "magenta", "hotpink", "palevioletred"]

x = 210
y = 210
size = 200
width = 16



def fractal(x, y, size, width):
    if size < 25:
        return
    else: 
        make_squares(x, y, size, width)

        fractal(x - size / 2, y - size / 2, size / 2, width / 2)
        fractal(x - size / 2, y + size / 2, size / 2, width / 2)
        fractal(x + size / 2, y - size / 2, size / 2, width / 2)
        fractal(x + size / 2, y + size / 2, size / 2, width / 2)

fractal(x, y, size, width)

root.mainloop()