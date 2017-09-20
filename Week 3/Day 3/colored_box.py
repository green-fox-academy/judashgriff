from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# draw a box that has different colored lines on each edge.

red_line = canvas.create_line(10, 10, 290, 10, fill='red')
blue_line = canvas.create_line(10, 10, 10, 290, fill='blue')
green_line = canvas.create_line(10, 290, 290, 290, fill='green')
yellow_line = canvas.create_line(290, 10, 290, 290, fill='yellow')

root.mainloop()