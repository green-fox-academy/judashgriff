
''' This program supposed to take your work hours daily - when you arrive, when you leave, lenght of 
breaks, and it should calculate your avereage work hours a day, your extra or minus hours, and your 
average break lenghts, and after each day it should provide all final data in a table form. '''


import time


temp_table = [{'Date': '09/17/14', 'work_minutes': 480, 'work_hours': "8:00", 'average_work': "8:00", 'break_minutes': 30, 'breaks_today': "0:30", 'average_breaks': "0:30", 'work_hour_index': "0:0"},
{'Date': '09/17/15', 'work_minutes': 360, 'work_hours': "6:00", 'average_work': "7:00", 'break_minutes': 90, 'breaks_today': "1:30", 'average_breaks': "1:00", 'work_hour_index': "-2:00"}
]

John_Doe_timetable = [
   {'Date': '09/17/14', 'work_hours': "8:00", 'average_work': "8:00", 'breaks_today': "0:30", 'average_breaks': "0:30", 'work_hour_index': "0:0"},
   {'Date': '09/17/15', 'work_hours': "6:00", 'average_work': "7:00", 'breaks_today': "1:30", 'average_breaks': "1:00", 'work_hour_index': "-2:00"}
]


# This is a universal time converter - which counts in mins. Really useful, I use it many times in this program.

def time_converter(item):
    time_in_minutes = item.split(':')
    time_in_minutes = int(time_in_minutes[0]) * 60 + int(time_in_minutes[1])
    return time_in_minutes


# The time querry.



start_time = input("Welcome! Please enter your starting time in the following format: \'10:30\' or \'14:00\': ")
start_time = time_converter(start_time)

finish_time = input("Please enter your finising time in the following format: \'15:30\' or \'19:00\': ")
finish_time = time_converter(finish_time) 

break_time = input("Please enter the length of your total breaks in the following format: \'0:30\' or \'1:10\': ")
break_time_minutes = time_converter(break_time) 


# Exact time counter - in minutes, and back to time format.


def exact_work_mins(start_time, finish_time, break_time):
    exact_work_mins = finish_time - start_time - break_time_minutes
    return exact_work_mins


def exact_work_time(start_time, finish_time, break_time):
    exact_work = ""
    exact_hours = (finish_time - start_time - break_time_minutes) //60
    exact_minutes = (finish_time - start_time - break_time_minutes) % 60
    exact_work = str(exact_hours) + ":" + str(exact_minutes)
    return exact_work


# Average time counter section.


def average_boss(timetable):
    return sum_of_worktime(timetable), sum_of_breaks(timetable)


def sum_of_worktime(timetable):
    sum_of_worktime = 0
    for day in timetable:
        if day['work_hours'] == 0:
            sum_of_worktime = 0
        else:
            sum_of_worktime += day['work_minutes']
    return average_work(sum_of_worktime)


def average_work(sum_of_work_minutes):
    if len(temp_table) > 0:
        average_work = sum_of_work_minutes / len(temp_table) 
    else:
        average_work = sum_of_work_minutes
    average_work = int(average_work)
    return average_work


def sum_of_breaks(timetable):
    sum_of_breaks = 0
    for day in timetable:
        if day['breaks_today'] == 0:
            sum_of_breaks = 0
        else:
            sum_of_breaks += day['break_minutes']
    return average_breaks(sum_of_breaks)


def average_breaks(sum_of_break_minutes):
    if len(temp_table) > 0:
        average_breaks = sum_of_break_minutes / len(temp_table)
    else:
        average_breaks = sum_of_break_minutes
    average_breaks = int(average_breaks)
    return average_breaks


# Temp table provider especially for exact daily minutes.


def add_to_temp_table(temp_timetable):
    temp_timetable.append({'work_minutes': exact_work_mins, 'work_hours': exact_work, 'average_work': 0, 'break_minutes': break_time_minutes, 'breaks_today': break_time, 'average_breaks': 0, 'work_hour_index': ""})


# The real John_Doe table supporter.


def add_to_John_Doe():
    John_Doe_timetable.append({'work_hours': exact_work, 'average_work': time_format_average_work, 'breaks_today': break_time, 'average_breaks': time_format_average_breaks, 'work_hour_index': index})
    return John_Doe_timetable


# Time format transformer for average times with one minute count input.


def average_time_forms(time_in_minutes):
    average_time_forms = ""
    average_hours = time_in_minutes //60
    average_minutes = time_in_minutes % 60
    average_time_forms = str(average_hours) + ":" + str(average_minutes)
    return average_time_forms


def create_index():
    index_in_minutes = 0
    for each in temp_table:
        index_in_minutes += each['work_minutes'] - 8 * 60
    index_time_form = average_time_forms(index_in_minutes)
    return index_time_form


exact_work_mins = exact_work_mins(start_time, finish_time, break_time)
exact_work = exact_work_time(start_time, finish_time, break_time)

print("\nYour exact work hours today: " + exact_work + ".\n")

add_to_temp_table(temp_table)

# Minute format for average works and breaks

average_work, average_breaks = average_boss(temp_table)

# Time format for average works and breaks  Work here !!!

time_format_average_work, time_format_average_breaks = average_time_forms(average_work), average_time_forms(average_breaks)

index = create_index()

add_to_John_Doe()


# Table form creator.


def printer():
    linear = "+" 
    for i in range(15):
        linear += "-"
    linear += "+"
    second_and_third_column(linear)
    return
    
    
def second_and_third_column(linear):
    second_column = 15
    third_column = 15
    fourth_column = 15
    fifth_column = 15
    sixth_column = 15
    for i in range(second_column):
        linear += "-"
    linear += "+"
    for i in range(third_column):
        linear += "-"
    linear += "+"
    for i in range(fourth_column):
        linear += "-"
    linear += "+"
    for i in range(fifth_column):
        linear += "-"
    linear += "+"   
    for i in range(sixth_column):
        linear += "-"
    linear += "+"   
    print(linear)
    header(linear, second_column, third_column, fourth_column, fifth_column, sixth_column)
    return 


def header(linear, second, third, fourth, fifth, sixth):
    header = "|"
    date = " Date" + (15 - len(" Date")) * " "
    work_hours = " Work hours" + (15 - len(" Work hours")) * " "
    work_average = " Average work" + (15 - len(" Average work")) * " "
    break_time = " Break today"  + (15 - len(" Break today")) * " "
    break_average = " Break average" + (15 - len(" Break average")) * " "
    index = " Work index" + (15 - len(" Work index")) * " "
    header += date + "|" + work_hours + "|" + work_average + "|" + break_time + "|" + break_average + "|" + index + "|" 
    print(header)
    print(linear)
    content(linear, second, third, fourth, fifth, sixth)
    return


def content(linear, second, third, fourth, fifth, sixth):
    for each in John_Doe_timetable:
        line = ""
        line += "| "
        line += str(time.strftime("%x"))
        line += ((15 - 8) - 1) * " " + "| "
        line += each['work_hours']
        line += (15 - len(each['work_hours']) - 1) * " " + "| "
        line += each['average_work']
        line += (15 - len(each['average_work']) - 1) * " " + "| "
        line += each['breaks_today']
        line += (15 - len(each['breaks_today']) - 1) * " " + "| "
        line += each['average_breaks']
        line += (15 - len(each['average_breaks']) - 1) * " " + "| "
        line += each['work_hour_index']
        line += (15 - len(each['work_hour_index']) - 1) * " " + "| "
        print(str(line))
    print(linear)
    return


printer()