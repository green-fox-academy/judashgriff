from tkinter import *


root = Tk()

canvas = Canvas(root, width='600', height='600', bd=0, highlightthickness=0)
canvas.pack()

def make_beehive_thing(limit, a,b,c,d,e,f,g,h,i,j,k,l):
    if limit == 1:
        pass
    else:
        canvas.create_polygon(a,b, c,d, e,f, g,h, i,j, k,l, fill ='', outline='black')
        limit -=1
        make_beehive_thing(limit, (a + (k-a)/2),(b + (l-b)/2),c,(d - (d-l)/2),(e - (e-k)/2),(f - (f-l)/2),(k + (i-k)/3*2),(j + (h-j)/2),(i - (i-k)/2),j,k,l)
        make_beehive_thing(limit, a,b,c,d,e,f,g,h,i,j,k,l)
        make_beehive_thing(limit, a,b,c,d,e,f,g,h,i,j,k,l)


# canvas.create_polygon([150,75,225,0,300,75,225,150, 200, 200], outline='gray', fill='gray', width=2)

limit = 5
a = 80 
b = 300   
c = 175 
d = 505
e = 425
f = 505 
g = 520
h = 300
i = 425
j = 95
k = 175
l = 95

size = 600/3
make_beehive_thing(limit, a,b,c,d,e,f,g,h,i,j,k,l)
root.mainloop()
