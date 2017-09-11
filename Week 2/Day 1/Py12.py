# Write a program that stores 3 sides of a cuboid as variables (doubles)
# The program should write the surface area and volume of the cuboid like:
# 
# Surface Area: 600
# Volume: 1000

a = 20
b = 40
c = 60

#Surface Area = (a*b)*2+(a*c)*2+(b*c)*2
print ("Surface Area is " + str(a*b*2+a*c*2+b*c*2) + " cubic cm-s")
print ("Volume is " + str(a*b*c) + " cubic cm-s")