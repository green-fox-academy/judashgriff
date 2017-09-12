# - Create a function called `factorio`
#   that returns it's input's factorial

def factorio (arg):
    index = 0
    while arg > 0:
        index = arg + index
        arg -= 1
    return index


print (factorio(3))