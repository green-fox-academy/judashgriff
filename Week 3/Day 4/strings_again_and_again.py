# Given a string, compute recursively a new string where all the
# adjacent chars are now separated by a "*".


def change_x_to_y(string):
    if len(string) == 1:
        return string
    else:
        return string[0] + "*" + change_x_to_y(string[1:])



string = "A szaxofonos xilofonra váltott."

changed = change_x_to_y(string)
print(changed)