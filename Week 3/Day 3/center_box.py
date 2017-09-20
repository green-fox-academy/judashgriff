from tkinter import *
from random import randint, choice

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# create a square drawing function that takes 1 parameter:
# the square size
# and draws a square of that size to the center of the canvas.
# draw 3 squares with that function.

def box_drawing(size):
    origo = get_origo(size)
    box = canvas.create_rectangle(origo, origo, origo + size, origo + size, fill=choice(colors))


def get_origo(size):
    origo = 150 - size / 2
    return origo


colors = ["red", "yellow", "pink", "blue", "gray", "red", "tomato"]

box_drawing(randint(0, 300))
box_drawing(randint(0, 300))
box_drawing(randint(0, 300))

root.mainloop()