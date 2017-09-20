from tkinter import *
from random import randint
root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# create a line drawing function that takes 2 parameters:
# the x and y coordinates of the line's starting point
# and draws a line from that point to the center of the canvas.
# draw 3 lines with that function.


def line_drawing(x_coordinate, y_coordinate):
    line = canvas.create_line(x_coordinate, y_coordinate, 150, 150)
    return


# def first_querry():
#     for lines in range(3):
#         x_coordinate = int(input("Yo guys, what the hell is going on?! Gimme the x coordinate number for the " + str(lines + 1) + "st. line!: "))
#         y_coordinate = int(input("Gimme the y coordinate number for the " + str(lines + 1) + "st. line!: "))
#         line_drawing(x_coordinate, y_coordinate)
#     return


# first_querry()


line_drawing(randint(0, 300), randint(0, 300))
line_drawing(randint(0, 300), randint(0, 300))
line_drawing(randint(0, 300), randint(0, 300))

root.mainloop()