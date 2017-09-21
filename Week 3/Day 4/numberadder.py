# Write a recursive function that takes one parameter: n and adds numbers from 1 to n.

def number_adder(n):
    if 1 == n:
        return n
    else:
        return n + number_adder(n-1)

n = 3
sum_of_total = number_adder(n)

print(sum_of_total)
