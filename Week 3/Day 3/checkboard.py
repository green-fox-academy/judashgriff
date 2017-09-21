from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# fill the canvas with a checkerboard pattern.


# def create_checkboard(checkboard):
#     for each in range(9):
#         box = canvas.create_rectangle(0 + (each - 1) * checkboard, 0 + (each - 1) * checkboard, checkboard * each, checkboard * each, fill='black')
#     return create_down(checkboard), create_right(checkboard)


# def create_down(checkboard):
#     for each in range(7):
#         box = canvas.create_rectangle(0 + (each - 1) * checkboard, 0 + checkboard * 2 + (each - 1) * checkboard, checkboard * each, checkboard * 2 + checkboard * each, fill='black')
#     for each in range(5):
#         box = canvas.create_rectangle(0 + (each - 1) * checkboard, 0 + checkboard * 4 + (each - 1) * checkboard, checkboard * each, checkboard * 4 + checkboard * each, fill='black')
#     for each in range(3):
#         box = canvas.create_rectangle(0 + (each - 1) * checkboard, 0 + checkboard * 6 + (each - 1) * checkboard, checkboard * each, checkboard * 6 + checkboard * each, fill='black')
#     return


# def create_right(checkboard):
#     for each in range(7):
#         box = canvas.create_rectangle(0 + checkboard * 2 + (each - 1) * checkboard, 0 + (each - 1) * checkboard, checkboard * 2 + checkboard * each, checkboard * each, fill='black')
#     for each in range(5):
#         box = canvas.create_rectangle(0 + checkboard * 4 + (each - 1) * checkboard, 0 + (each - 1) * checkboard, checkboard * 4 + checkboard * each, checkboard * each, fill='black')
#     for each in range(3):
#         box = canvas.create_rectangle(0 + checkboard * 6 + (each - 1) * checkboard, 0 + (each - 1) * checkboard, checkboard * 6 + checkboard * each, checkboard * each, fill='black')
#     return


def create_checkboard(checkboard):
    for i in range(9):
        for j in range(9):
            canvas.create_rectangle(0 + (j*2) * checkboard, 0 + (i*2) * checkboard, checkboard + (j*2) * checkboard,  checkboard + (i*2) * checkboard, fill='black')
            canvas.create_rectangle(checkboard + (j*2) * checkboard, checkboard + (i*2) * checkboard, 2*checkboard + checkboard * (j*2), 2*checkboard + checkboard * (j*2), fill='black')                


checkboard = 305/8

create_checkboard(checkboard)

root.mainloop()