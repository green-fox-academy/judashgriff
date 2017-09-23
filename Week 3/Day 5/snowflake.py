from tkinter import *
import time

root = Tk()

canvas = Canvas(root, width='420', height='500', bd=0, highlightthickness=0)
canvas.pack()

def snowflake(x,y,size):
    canvas.create_polygon(x, y + size / 4,
                          x + size / 3, y + size / 4,
                          x + size / 2, y,
                          x + (size / 3) * 2, y + size / 4,
                          x + size, y + size / 4,
                          x + (size / 6) * 5, y + size /2,
                          x + size, y + (size / 4) * 3,
                          x + (size / 3) * 2, y + (size / 4) * 3,
                          x + size / 2, y + size,
                          x + size / 3, y + (size / 4) * 3,
                          x , y + (size / 4) * 3,
                          x + size / 6, y + size / 2,
                          fill = 'white', outline='black')



def draw_fractal(x, y, size):
    time.sleep(0.1)
    canvas.update()
    if size < 5:
        return
    else:
        snowflake(x, y, size)

        draw_fractal(x, y + size / 6, size / 3)
        draw_fractal(x + (size / 3) / 3, y + (size / 4) / 3, size / 3)
        draw_fractal(x + size / 2 - (size / 3) * 2, y + (size / 12) * 3, size / 3)
        draw_fractal(x + ((size / 3) / 3) * 2, y + (size / 4) / 3, size / 3)
        draw_fractal(x + size / 3, y + size / 6, size / 3)
        draw_fractal(x + (size / 3) - size / (3*3*3), y + (size / 6) * 1.5 , size / 3)

        draw_fractal(x + size / 3, y + size / 6 * 2, size / 3)
        draw_fractal(x + ((size / 3) / 3) * 2, y + (size / 4) / 3 * 2, size / 3)
        draw_fractal(x + size / 2 - (size / 3) * 2, y + size / 2, size / 3)

        # draw_fractal(x + (size / 3) * 2, y + (size / 3) * 2, size / 3)
        # draw_fractal(x + (size / 3) * 2, y + (size / 3) * 2, size / 3)
        # draw_fractal(x + (size / 3) * 2, y + (size / 3) * 2, size / 3)


x = 10
y = 10
size = 400

draw_fractal(x, y, size)


root.mainloop()
