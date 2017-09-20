from tkinter import *
from random import randint, choice

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# create a line drawing function that takes 2 parameters:
# the x and y coordinates of the line's starting point
# and draws a line from that point to the center of the canvas.
# fill the canvas with lines from the edges, every 20 px, to the center.

def make_one_line(num_x, num_y):
     canvas.create_line(num_x, num_y, 150, 150, fill='black')
     

def make_lines_round():
    for i in range(16):
        canvas.create_line(0 + (i - 1) * 20, 0, 150, 150, fill=choice(color))
    for i in range(16):
        canvas.create_line(0, 0 + (i - 1) * 20, 150, 150, fill=choice(color))
    for i in range(16):
        canvas.create_line(150, 150, 300, 0 + (i - 1) * 20, fill=choice(color))
    for i in range(16):
        canvas.create_line(150, 150, 0 + (i - 1) * 20, 300, fill=choice(color))


make_one_line(randint(0, 300), randint(0, 300))
color = ["blue", "pink", "red", "tomato", "yellow", "gray", "orange", "blue", "green", "turquoise", "magenta", "cyan"]
make_lines_round()

root.mainloop()