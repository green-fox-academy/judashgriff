from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# reproduce this:
# [https://github.com/greenfox-academy/teaching-materials/blob/master/workshop/drawing/purple-steps/r3.png]

def create_first_box(box_size):
    box = canvas.create_rectangle(10, 10, 10 + box_size, 10 + box_size, fill='indigo')
    return multiply_boxes(box_size)


def multiply_boxes(box_size):
    for each in range(20):
        box = canvas.create_rectangle( 10 * (each + 1) + box_size,  10 * (each + 1) + box_size, 10 * (each + 2) + box_size, 10 * (each + 2) + box_size, fill='indigo')
    return



box_size = 10

create_first_box(box_size)

root.mainloop()