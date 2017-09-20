from tkinter import *
from random import randint, choice


root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# draw the night sky:
# - The background should be black
# - The stars should be small squares
# - The stars should have random positions on the canvas
# - The stars should have random color (some shade of grey)

def make_black_sky():
    canvas.create_rectangle(0,0,300,300, fill = 'black')

def make_the_stars():
    for i in range(25):
        a = randint(5, 290)
        b = randint(5, 290) 
        canvas.create_rectangle(a, b, a+5, b+5, fill=choice(colors))

colors = ["dimgrey", "silver", "gray", "lightgray", "whitesmoke"]

make_black_sky()
make_the_stars()

root.mainloop()