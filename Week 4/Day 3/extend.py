import statistics

# Adds a and b, returns as result
def add(a, b):
    c = a + b
    return c

# Returns the highest value from the three given params
def max_of_three(a, b, c):
    return max(a, b, c)

# Returns the median value of a list given as param
def median(pool):
    if pool == 0 or  pool == []:
        return False
    return statistics.median(pool)

# Returns true if the param is a vowel
def is_vovel(char):
    return char.lower() in 'aáeéiíoóöőuúüű'

# Create a method that translates hungarian into the teve language
def translate(hungarian):
    teve = ""
    for char in hungarian:
        if is_vovel(char):
            teve += char + "v" + char
        else:
            teve += char
    return teve