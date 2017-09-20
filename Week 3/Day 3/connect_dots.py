from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# create a function that takes 1 parameter:
# a list of [x, y] points
# and connects them with green lines.
# connect these to get a box: [[10, 10], [290,  10], [290, 290], [10, 290]]
# connect these: [[50, 100], [70, 70], [80, 90], [90, 90], [100, 70],
# [120, 100], [85, 130], [50, 100]]

def connect_lines(list1):
    for i in range(len(list1)):
        canvas.create_line(list1[i-1][0], list1[i-1][1], list1[i][0], list1[i][1], fill = 'green')


list1 =  [[10, 10], [290,  10], [290, 290], [10, 290]]
list2 = [[50, 100], [70, 70], [80, 90], [90, 90], [100, 70], [120, 100], [85, 130], [50, 100]]

connect_lines(list2)

root.mainloop()