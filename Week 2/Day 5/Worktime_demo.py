
''' This program supposed to take your work hours daily - when you arrive, when you leave, lenght of 
breaks, and it should calculate your avereage work hours a day, your extra or minus hours, and your 
average break lenghts, and after each day it should provide all final data in a table form. '''

temp_table = []

John_Doe_timetable = [
#    {'work_hours': "8:00", 'average_work': "8:00", 'breaks_today': "0:30", 'average_breaks': "0:30", 'work_hour_index': "0:0"}
]


def time_converter(item):
    time_in_minutes = item.split(':')
    time_in_minutes = int(time_in_minutes[0]) * 60 + int(time_in_minutes[1])
    return time_in_minutes


start_time = input("Welcome! Please enter your starting time in the following format: \'10:30\' or \'14:00\': ")
start_time = time_converter(start_time)

finish_time = input("Please enter your finising time in the following format: \'15:30\' or \'19:00\': ")
finish_time = time_converter(finish_time) 

break_time = input("Please enter the length of your total breaks in the following format: \'0:30\' or \'1:10\': ")
break_time_minutes = time_converter(break_time) 


def exact_work_mins(start_time, finish_time, break_time):
    exact_work_mins = finish_time - start_time - break_time_minutes
    return exact_work_mins


def exact_work_time(start_time, finish_time, break_time):
    exact_work = ""
    exact_hours = (finish_time - start_time - break_time_minutes) //60
    exact_minutes = (finish_time - start_time - break_time_minutes) % 60
    exact_work = str(exact_hours) + ":" + str(exact_minutes)
    return exact_work


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
    if len(John_Doe_timetable) > 0:
        average_work = sum_of_work_minutes / len(John_Doe_timetable)
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
    if len(John_Doe_timetable) > 0:
        average_breaks = sum_of_break_minutes / len(John_Doe_timetable)
    else:
        average_breaks = sum_of_break_minutes
    average_breaks = int(average_breaks)
    return average_breaks


def add_to_temp_table(temp_timetable):
    temp_timetable.append({'work_minutes': exact_work_mins, 'work_hours': exact_work, 'average_work': "", 'break_minutes': break_time_minutes, 'breaks_today': break_time, 'average_breaks': "", 'work_hour_index': ""})


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
    if index_in_minutes < 0:
        index_time_form = average_time_forms(index_in_minutes)
    elif index_in_minutes >= 0: 
        index_time_form = average_time_forms(index_in_minutes)
    return index_time_form


def add_to_John_Doe():
    John_Doe_timetable.append({'work_hours': exact_work, 'average_work': time_format_average_work, 'breaks_today': break_time, 'average_breaks': time_format_average_breaks, 'work_hour_index': index})
    return John_Doe_timetable

exact_work_mins = exact_work_mins(start_time, finish_time, break_time)
exact_work = exact_work_time(start_time, finish_time, break_time)

print("Your exact work hours today: " + exact_work + ".")

add_to_temp_table(temp_table)

average_work, average_breaks = average_boss(temp_table)

time_format_average_work = average_time_forms(average_work)
time_format_average_breaks = average_time_forms(average_breaks)


# print("The average work hours so far: " + John_Doe_timetable['time_format_average_work'] + ". Your average break length is: " + John_Doe_timetable['time_format_average_breaks'] + ".")

index = create_index()

print(add_to_John_Doe())