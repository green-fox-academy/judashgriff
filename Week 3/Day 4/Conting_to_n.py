# Write a recursive function that takes one parameter: n and counts down from n.


def counter(num):
    if num == 0:
        return num
    else:
        print(num)
        return counter(num-1)

num = 5
counter(num)