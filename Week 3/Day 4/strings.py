# Given a string, compute recursively (no loops) a new string where all the
# lowercase 'x' chars have been changed to 'y' chars.

def change_x_to_y(string):
    if len(string) == 0:
        return string
    elif string[0] == "x":
        return "y" + change_x_to_y(string[1:])
    else:
        return string[0] + change_x_to_y(string[1:])



string = "A szaxofonos xilofxonxra vxáxlxtoXtXt."

changed = change_x_to_y(string)
print(changed)