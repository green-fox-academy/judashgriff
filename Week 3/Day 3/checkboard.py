from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300', highlightthickness=0)
canvas.pack()


def create_checkboard(size):
    for row in range(9):
        for column in range(9):
            if (row + column) % 2 == 0:
                canvas.create_rectangle(column * size, row * size, 
                (column + 1) * size, (row + 1) * size, fill='black')


size = 300/8

create_checkboard(size)

root.mainloop()