def dig_pow(n, p):
    k = 0
    for i, char in enumerate(str(n)):
        k += pow(int(char), p + i)
    return int(k / n) if k % n == 0 else -1


print(dig_pow(46288, 3))