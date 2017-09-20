from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# reproduce this:
# [https://github.com/greenfox-academy/teaching-materials/blob/master/workshop/drawing/purple-steps-3d/r4.png]

def create_boxes(box_size):
    base = 0
    for each in range(7):
        box = canvas.create_rectangle((each + 1) * 10 + base, (each + 1) * 10 + base, (each + 1) * 20 + base, (each + 1) * 20 + base, fill='purple')
        base += each * 10


box_size = 10

create_boxes(box_size)

root.mainloop()