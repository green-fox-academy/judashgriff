
students = [
        {'name': 'Teodor', 'age': 3, 'candies': 2},
        {'name': 'Rezso', 'age': 9.5, 'candies': 2},
        {'name': 'Zsombor', 'age': 12, 'candies': 5},
        {'name': 'Aurel', 'age': 7, 'candies': 3},
        {'name': 'Olaf', 'age': 12, 'candies': 7},
        {'name': 'Gerzson', 'age': 10, 'candies': 1},
]

# create a function that takes a list of students and prints: 
# - how many candies are owned by students

# create a function that takes a list of students and prints:
# - Sum of the age of people who have lass than 5 candies



def names(students):
    candy = []
    for i in students:
        temp = {}
        temp['name'] = i['name']
        temp['candies'] = i['candies']
        candy.append(temp)
    return candy

def age(students):
    ages = []
    for i in students:
        temp = {}
        if i['candies'] < 5: 
            temp['name'] = i['name']
            temp['age'] = i['age']
            ages.append(temp)
    return ages


candy = names(students)

ages = age(students)

sum_of_ages = 0

for i in ages:
    sum_of_ages += i['age']

averages = sum_of_ages / len(ages)

print (candy)
print (averages)