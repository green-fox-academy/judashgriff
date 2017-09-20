from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# reproduce this:
# [https://github.com/greenfox-academy/teaching-materials/blob/master/workshop/drawing/purple-steps-3d/r4.png]

def create_boxes(box_size):
    base = 0
    for each in range(6):
        box = canvas.create_rectangle((each + 1) * box_size + base, (each + 1) * box_size + base, (each + 1) * (box_size * 2) + base, (each + 1) * (box_size * 2) + base, fill='purple')
        base += each * box_size


box_size = 10

create_boxes(box_size)

root.mainloop()