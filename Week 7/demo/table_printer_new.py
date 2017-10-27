# +--------------------+---------------+----------+
# | Ingredient         | Needs cooling | In stock |
# +--------------------+---------------+----------+
# | vodka              | Yes           | 1        |
# | coffee_liqueur     | Yes           | -        |
# | fresh_cream        | Yes           | 1        |
# | captain_morgan_rum | Yes           | 2        |
# | mint_leaves        | No            | -        |
# +--------------------+---------------+----------+

ingredients = [
	{ "name": "vodka", "in_stock": 1, "needs_cooling": True },
	{ "name": "coffee_liqueur", "in_stock": 0, "needs_cooling": True },
	{ "name": "fresh_cream", "in_stock": 1, "needs_cooling": True },
	{ "name": "captain_morgan_rum", "in_stock": 2, "needs_cooling": True },
	{ "name": "mint_leaves", "in_stock": 0, "needs_cooling": False },
	{ "name": "sugar", "in_stock": 0, "needs_cooling": False },
	{ "name": "lime juice", "in_stock": 0, "needs_cooling": True },
	{ "name": "soda", "in_stock": 0, "needs_cooling": True }
]

def print_line(length):
    section1 = "+";
    section1 += add_lines(length)
    section1 += add_lines(15)
    section1 += add_lines(10)
    return section1

   
def the_length():
    length = 0
    for element in ingredients:
        if length < len(element["name"]):
            length = len(element["name"])
    length += 2
    return length

def add_lines(num):
    section = ""
    for i in range(num):
        section += "-"
    section += "+"
    return section

def print_head(length):
    head = "|"
    head += add_content("Ingridient", length)
    head += add_content("Needs cooling", 15)
    head += add_content("In stock", 10)
    return head

def add_content(text, length):
    content = " "
    content += str(text)
    for i in range(length - len(content)):
        content += " "
    content += "|"
    return content

def add_body(element, length):
    body = "|"
    body += add_content(element["name"], length)
    if element["needs_cooling"] == True:
        body += add_content("Yes", 15)
    else:
        body += add_content("No", 15)
    if element["in_stock"] > 0:
        body += add_content(element["in_stock"], 10)
    else:
        body += add_content("-", 10)
    return body

def print_boss():
    length = the_length()
    line = print_line(length)
    head = print_head(length)
    print(line)
    print(head)
    print(line)
    for element in ingredients:
        body = add_body(element, length)
        print(body)
    print(line)

print_boss()