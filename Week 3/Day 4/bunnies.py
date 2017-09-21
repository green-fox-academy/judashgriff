# We have a number of bunnies and each bunny has two big floppy ears.
# We want to compute the total number of ears across all the bunnies recursively (without loops or multiplication).

def get_bunny_ears(bunnies):
    if bunnies == 1:
        return 2
    else:
        return 2 + get_bunny_ears(bunnies-1)


bunnies = 562

ears = get_bunny_ears(bunnies)
print(ears)