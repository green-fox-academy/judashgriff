# - Create an array variable named `ag`
#   with the following content: `[3, 4, 5, 6, 7]`
# - Double all the values in the array

ag = [3, 4, 5, 6, 7]

def double(lst):
    for i, x in enumerate(lst):
        x *= 2
        print("x = %s" % x)
        print("lst[%d] = %s" % (i, lst[i]))

print (double(ag))
