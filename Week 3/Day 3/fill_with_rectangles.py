from tkinter import *
from random import randint

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# draw four different size and color rectangles.

green_box = canvas.create_rectangle(randint(0, 300), randint(0, 300), randint(0, 300), randint(0, 300), fill='green')
green_box = canvas.create_rectangle(randint(0, 300), randint(0, 300), randint(0, 300), randint(0, 300), fill='blue')
green_box = canvas.create_rectangle(randint(0, 300), randint(0, 300), randint(0, 300), randint(0, 300), fill='yellow')
green_box = canvas.create_rectangle(randint(0, 300), randint(0, 300), randint(0, 300), randint(0, 300), fill='red')


root.mainloop()