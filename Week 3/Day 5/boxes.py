from tkinter import *
import time

root = Tk()

canvas = Canvas(root, width='400', height='400', bd=0, highlightthickness=0)
canvas.pack()

def box(x,y,size):
    canvas.create_rectangle(x, y, x + size, y + size, fill = '', outline='')
    canvas.create_rectangle(x + size / 3, y + size / 3, x + (size / 3) * 2, y + (size / 3) * 2,  fill = 'black', outline='')


def draw_fractal(x,y,size):
    time.sleep(0.00000001)
    canvas.update()
    if size < 2:
        return
    else:
        box(x, y, size)

        draw_fractal(x, y, size / 3)
        draw_fractal(x + size / 3, y, size / 3)
        draw_fractal(x + (size / 3) * 2, y, size / 3)

        draw_fractal(x, y + size / 3, size / 3)
        draw_fractal(x + (size / 3) * 2, y + size / 3, size / 3)

        draw_fractal(x, y + (size / 3) * 2, size / 3)
        draw_fractal(x + size / 3, y + (size / 3) * 2, size / 3)
        draw_fractal(x + (size / 3) * 2, y + (size / 3) * 2, size / 3)


x = 0
y = 0
size = 400

draw_fractal(x, y, size)


root.mainloop()
