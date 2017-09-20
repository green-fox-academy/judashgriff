from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# reproduce this:
# [https://github.com/greenfox-academy/teaching-materials/blob/master/workshop/drawing/envelope-star/r2.png]

def make_envelope_star():
    for each in range(16):
         canvas.create_line(0 + (each - 1) * 10, 150, 150, 140 - (each) * 10, fill='green')
    for each in range(16):
         canvas.create_line(300 - (each - 1) * 10, 150, 150 , 140 - (each) * 10, fill='green')
    for each in range(16):
         canvas.create_line(0 + (each - 1) * 10, 150, 150, 160 + (each) * 10, fill='green')
    for each in range(16):
         canvas.create_line(300 - (each - 1) * 10, 150, 150, 160 + (each) * 10, fill='green')
    canvas.create_line(150, 0, 150, 300, fill='green')

make_envelope_star()

root.mainloop()