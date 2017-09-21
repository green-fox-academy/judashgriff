# Write a recursive function that takes one parameter: n and adds numbers from 1 to n.

def number_adder(n, out):
    base = 1
    if base == n:
        out += 1
        print(out)
        return
    else:
        out += n
        number_adder(n-1, out)
out = 0

n = 980
number_adder(n, out)
