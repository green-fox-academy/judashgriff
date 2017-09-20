from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# reproduce this:
# [https://github.com/greenfox-academy/teaching-materials/blob/master/workshop/drawing/line-play/r1.png]

def make_green_lines():
    for each in range(15):
        canvas.create_line(0, 20 + (each - 1) * 19, 20 + (each - 1) * 19, 300, fill='green')


def make_purple_lines():
    for each in range(15):
        canvas.create_line(20 + (each - 1) * 19, 0, 300, 19 + (each - 1) * 19, fill='purple')


make_green_lines()
make_purple_lines()

root.mainloop()


