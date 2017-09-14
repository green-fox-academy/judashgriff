# Create a function that prints the ingredient list of dictionaries to the console in the following format:
#
# +--------------------+---------------+----------+
# | Ingredient         | Needs cooling | In stock |
# +--------------------+---------------+----------+
# | vodka              | Yes           | 1        |
# | coffee_liqueur     | Yes           | -        |
# | fresh_cream        | Yes           | 1        |
# | captain_morgan_rum | Yes           | 2        |
# | mint_leaves        | No            | -        |
# +--------------------+---------------+----------+
#
# OPTIONAL:
# The frist columns should be automatically as wide as the longest key

ingredients = [
	{ "name": "vodka", "in_stock": 1, "needs_cooling": True },
	{ "name": "coffee_liqueur", "in_stock": 38887, "needs_cooling": True },
	{ "name": "fresh_cream", "in_stock": 1, "needs_cooling": True },
	{ "name": "captain_morgan_rum_ala_huhhahahahhahahahaha", "in_stock": 2, "needs_cooling": True },
	{ "name": "mint_leaves", "in_stock": 0, "needs_cooling": False },
	{ "name": "sugar", "in_stock": 0, "needs_cooling": False },
	{ "name": "lime juice", "in_stock": 0, "needs_cooling": True },
	{ "name": "soda", "in_stock": 0, "needs_cooling": True }
]

def width_collector(item):
    List = []
    for i in item:
        List.append(i['name'])
    width_counter(List)
    return


def width_counter(List_item):
    first_column = len(max(List_item, key=len)) + 1
    printer(first_column)
    return


def printer(first):
    linear = "+" 
    for i in range(first):
        linear += "-"
    linear += "+"
    second_and_third_column(linear, first)
    return
    
    
def second_and_third_column(linear, first):
    second_column = 15
    third_column = 10
    for i in range(second_column):
        linear += "-"
    linear += "+"
    for i in range(third_column):
        linear += "-"
    linear += "+"
    print(linear)
    header(linear, first, second_column, third_column)
    return 


def header(linear, first, second, third):
    header = "|"
    ingridient = " Ingredient "
    cooling = " Needs cooling "
    stock = " In stock "
    header += ingridient
    more = (first - len(ingridient)) * " "
    header += more 
    header += "|" + cooling + "|" + stock + "|"
    print(header)
    print(linear)
    content(linear, first, second, third)
    return


def content(linear, first, second, third):
    for each in ingredients:
        line = ""
        line += "| "
        line += each['name']
        line += (first - len(each['name']) - 1) * " " + "| "
        if each['needs_cooling'] is True: 
            line += "Yes" + (second - 4) * " " + "| "
        elif each['needs_cooling'] is False:
            line += "No" + (second - 3) * " " + "| "
        if each['in_stock'] > 0:
            line += str(each['in_stock'])
            line += (third - len(str(each['in_stock'])) - 1) * " "
        else:
             line += "-" + (third - len(str(each['in_stock'])) - 1) * " "
        line += "|"
        print(str(line))
    print(linear)
    return


width_collector(ingredients)