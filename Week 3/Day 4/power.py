# Given base and n that are both 1 or more, compute recursively (no loops)
# the value of base to the n power, so powerN(3, 2) is 9 (3 squared).

def get_power(base, n):
    if n == 1:
        return n * base
    else:
        return base * get_power(base, n-1)


base = 10
n = 5
power = get_power(base, n)

print(power)