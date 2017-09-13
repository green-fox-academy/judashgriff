students = [
        {'name': 'Rezso', 'age': 9.5, 'candies': 2},
        {'name': 'Gerzson', 'age': 10, 'candies': 1},
        {'name': 'Aurel', 'age': 7, 'candies': 3},
        {'name': 'Zsombor', 'age': 12, 'candies': 5}
]

# create a function that takes a list of students and prints:
# - Who has got more candies than 4 candies

# create a function that takes a list of students and prints: 
#  - how many candies they have on average

def morecandy(students):
    candy = []
    for i in range(len(students)):
        if students[i]['candies'] > 4:
            candy.append(students[i]['name'])
            candy.append(students[i]['candies'])
    return candy

def average(students):
    total = []
    for i in range(len(students)):
        total.append(students[i]['candies'])
    return total
        
more_than4 = morecandy(students)
total = average(students)

sum_of_total = 0

for i in range(len(total)):
    sum_of_total += total[i]

average_candy = sum_of_total / len(total)

print (more_than4)
print (average_candy)