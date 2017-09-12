# - Write a function called `sum` that sum all the numbers
#   until the given parameter

def sum (num):
    part = 0
    while num>0:
        part = part + num
        num -= 1
    return part

print (sum(10))

