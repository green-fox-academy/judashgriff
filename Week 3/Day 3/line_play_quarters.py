from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# divide the canvas into 4 equal parts
# and repeat this pattern in each quarter:
# [https://github.com/greenfox-academy/teaching-materials/blob/master/workshop/drawing/line-play/r1.png]

def make_colorful_lines():
    for each in range(15):
        canvas.create_line(0, 10 + (each - 1) * 10, 10 + (each - 1) * 10, 150, fill='green')
    for each in range(15):
        canvas.create_line(150 + (each - 1) * 10, 0, 300, 10 + (each - 1) * 10, fill='purple')
    for each in range(15):
        canvas.create_line(0, 160 + (each - 1) * 10, 10 + (each - 1) * 10, 300, fill='green')
    for each in range(15):
        canvas.create_line(150 + (each - 1) * 10, 150, 300, 160 + (each - 1) * 10, fill='purple')
    for each in range(15):
        canvas.create_line(10 + (each - 1) * 10, 0, 150, 10 + (each - 1) * 10, fill='purple')
    for each in range(15):
        canvas.create_line(150, 10 + (each - 1) * 10, 160 + (each - 1) * 10, 150, fill='green')
    for each in range(15):
        canvas.create_line(10 + (each - 1) * 10, 150, 150, 160 + (each - 1) * 10, fill='purple')
    for each in range(15):
        canvas.create_line(150, 160 + (each - 1) * 10, 160 + (each - 1) * 10, 300, fill='green')


make_colorful_lines()



root.mainloop()