from tkinter import *
from random import randint, choice



root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# create a square drawing function that takes 2 parameters:
# the x and y coordinates of the square's top left corner
# and draws a 50x50 square from that point.
# draw 3 squares with that function.

def square_drawing(x_coordinate, y_coordinate):
    square = canvas.create_rectangle(x_coordinate, y_coordinate, x_coordinate+50, y_coordinate+50, fill=choice(colors))
    return


colors = ["red", "yellow", "pink", "blue", "gray", "red", "tomato"]

square_drawing(randint(0, 250), randint(0, 250))
square_drawing(randint(0, 250), randint(0, 250))
square_drawing(randint(0, 250), randint(0, 250))


root.mainloop()