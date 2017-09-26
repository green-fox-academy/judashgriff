class Person(object):
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    def introduce(self):
        print("Hi, my name is " + str(self.name) + ", a " + str(self.age) + " old " + str(self.gender))

    def get_goal(self):
        print("My goal is: Live for the moment!")



class Student(object):
    def __init__(self, name, age, gender, organisation):
        self.name = name
        self.age = age
        self.gender = gender
        self.previous_organisation = organisation
        self.skipped_days = 0

    def introduce(self):
        print( "Hi, I'm " + str(self.name) + ", a " + str(self.age) + " year old " 
        + str(self.gender) + " from " + str(self.previous_organisation) + " who skipped " 
        + str(self.skipped_days) + " days from the course already.")

    def get_goal(self):
        print("Be a junior software developer.")

    def skip_day(self):
        self.skipped_days += 1


class Mentor(object):
    def __init__(self, name, age, gender, level):
        self.name = name
        self.age = age
        self.gender = gender
        self.level = level
    
    def introduce(self):
        print("Hi, my name is " + str(self.name) + ", a " + str(self.age) + " old " 
        + str(self.gender) + " " + str(self.level) + " mentor.")

    def get_goal(self):
        print("Educate brilliant junior software developers.")


class Sponsor(object):
    def __init__(self, name, age, gender, company):
        self.name = name
        self.age = age
        self.gender = gender
        self.company = company
        self.hired_students = 0
    
    def introduce(self):
        print("Hi, my name is " + str(self.name) + ", a " + str(self.age) + " old " 
        + str(self.gender) + " who represents " + str(self.company) + " and hired " 
        + str(self.company) + " students so far.")

    def get_goal(self):
        print("Hire brilliant junior software developers.")

    def hired_students(self):
        self.hired_students += 1


Jane = Person('Jane Doe', 30, 'female')

Jane.introduce()
Jane.get_goal()

Jane = Student('Jane Doe', 30, 'female', 'The School of Life')

Jane.introduce()
Jane.get_goal()

Jane = Mentor('Jane Doe', 30, 'female', 'intermediate')

Jane.introduce()
Jane.get_goal()

Jane = Sponsor('Jane Doe', 30, 'female', 'Google')

Jane.introduce()
Jane.get_goal()