from tkinter import *
from random import randint

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# create a line drawing function that takes 2 parameters:
# the x and y coordinates of the line's starting point
# and draws a 50 long horizontal line from that point.
# draw 3 lines with that function.


def line_drawing(x_coordinate, y_coordinate):
    line = canvas.create_line(x_coordinate, y_coordinate, x_coordinate+50, y_coordinate)
    return


line_drawing(randint(0, 250), randint(0, 300))
line_drawing(randint(0, 250), randint(0, 300))
line_drawing(randint(0, 250), randint(0, 300))

root.mainloop()