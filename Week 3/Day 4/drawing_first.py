from tkinter import *


root = Tk()

canvas = Canvas(root, width='600', height='600', bg='yellow', bd=0, highlightthickness=0)
canvas.pack()


def make_thing(x, y, size):
    start_x = x + size
    start_y = y + size
    if size < 2:
        return
    else:
        canvas.create_rectangle(start_x, y, start_x+size, start_y)
        canvas.create_rectangle(x, start_y, start_x, start_y+size)
        canvas.create_rectangle(start_x+size, start_y, start_x+size*2, start_y+size)
        canvas.create_rectangle(start_x, start_y+size, start_x+size, start_y+size*2)
        return make_thing(start_x, y, size/3), make_thing(x, start_y, size/3), make_thing(start_x+size, start_y, size/3), make_thing(start_x, start_y+size, size/3)

size = 600/3
make_thing(0, 0, size)
root.mainloop()

