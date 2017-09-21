# Given a string, compute recursively a new string where all the 'x' chars have been removed.

def change_x_to_y(string):
    if len(string) == 1:
        return string
    elif string[0] == "x":
        return change_x_to_y(string[1:])
    else:
        return string[0] + change_x_to_y(string[1:])



string = "A szaxofonos xilofxonxra vxáxlxtoXtXt."

changed = change_x_to_y(string)
print(changed)