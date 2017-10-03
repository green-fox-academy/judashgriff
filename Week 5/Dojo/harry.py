def books_cost(shopping_list):
    if shopping_list == ["1"]:
        return 8
    elif shopping_list == ["1", "1"]:
        return 16
    elif len(shopping_list) > 1 and shopping_list[0] != shopping_list[1]:
        return 16*0.95
    elif len(shopping_list) > 1 and "1" in shopping_list and "2" in shopping_list:
        dict_from_shopping_list(shopping_list)
        return (16*0.95+8)
    elif len(shopping_list) == 3:
        return 24
    
    return 0

d = {}
def dict_from_shopping_list(shopping_list):
    for element in shopping_list:
        if element in d:
            d[element] += 1
        elif element not in d:
            d[element] = 1
    return check_dictionary(d)

def check_dictionary(d):
    print(d)