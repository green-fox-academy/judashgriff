def find_it(seq):
    dictionary = get_dict(seq)
    print(dictionary)
    odds = 0
    for each in dictionary:
        if dictionary[each] % 2 == 1:
            odds = each
    return odds
    
def get_dict(seq):
    dictionary = {}
    for each in seq:
        if each not in dictionary:
            dictionary[each] = 1
        elif each in dictionary:
            dictionary[each] += 1
    return dictionary

print(find_it([10]))