from tkinter import *
from random import randint, choice


root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

def make_triangle():
    canvas.create_polygon(150, 20, 142, 30)


def triangle(number_of_rows, triangle_size, margin):


triangle(number_of_rows=21, triangle_size=9, margin=10)
make_triangle()


root.mainloop()