from tkinter import *
from random import randint, choice


root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# create a square drawing function that takes 2 parameters:
# the square size, and the fill color,
# and draws a square of that size and color to the center of the canvas.
# create a loop that fills the canvas with rainbow colored squares.

def base_box_drawing(size, color):
    origo = get_origo(size)
    box = canvas.create_rectangle(origo, origo, origo + size, origo + size, fill=choice(colors))
    return rainbow_drawing(size, origo)


def get_origo(size):
    origo = 150 - size / 2
    return origo


def rainbow_drawing(size, origo):
    for numbering in range(7):
        canvas.create_rectangle(origo + 10 * (numbering + 2), origo + 10 * (numbering + 2), origo + size - 10 * (numbering + 2), origo + size - 10 * (numbering + 2), fill=rainbow[numbering])
    return



colors = ["red", "yellow", "pink", "blue", "gray", "red", "tomato"]

rainbow = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

base_box_drawing(randint(150, 300), choice(colors))

root.mainloop()
