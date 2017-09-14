
''' This program supposed to take your work hours daily - when you arrive, when you leave, lenght of 
breaks, and it should calculate your avereage work hours a day, your extra or minus hours, and your 
average break lenghts, and after each day it should provide all final data in a table form. '''

John_Doe_timetable = [
    {'work_hours': "", 'average_work': "", 'breaks_today': "", 'average_breaks': "", 'work_hour_index': ""},
    {'work_hours': "", 'average_work': "", 'breaks_today': "", 'average_breaks': "", 'work_hour_index': ""},
    {'work_hours': "", 'average_work': "", 'breaks_today': "", 'average_breaks': "", 'work_hour_index': ""}
]


def time_converter(item):
    time_in_minutes = item.split(':')
    time_in_minutes = int(time_in_minutes[0]) * 60 + int(time_in_minutes[1])
    return time_in_minutes


start_time = input("Welcome! Please enter your starting time in the following format: \'10:30\' or \'14:00\': ")
start_time = time_converter(start_time)
print(start_time)

finish_time = input("Please enter your finising time in the following format: \'15:30\' or \'19:00\': ")
finish_time = time_converter(finish_time) 

break_time = input("Please enter the length of your total breaks in the following format: \'0:30\' or \'1:10\': ")
break_time_minutes = time_converter(break_time) 


def exact_work_time(start_time, finish_time, break_time):
    exact_work = ""
    exact_hours = (finish_time - start_time - break_time_minutes) //60
    exact_minutes = (finish_time - start_time - break_time_minutes) % 60
    exact_work = str(exact_hours) + ":" + str(exact_minutes)
    print(exact_work)
    return exact_work


exact_work = exact_work_time(start_time, finish_time, break_time)


def export_data(exact_work, break_time):
    for day in John_Doe_timetable:


John_Doe_timetable[n]['work_hours'].append(str(exact_work))

case_list = {}
for entry in entries_list:
    if key in case_list:
        case_list[key1].append(value)
    else:
        case_list[key1] = [value]


# key, val = your_input.split(':')
# thing.update({key:val})


# In [126]: strs="""A1023 CRT
#    .....: A1029 Regulator
#    .....: A1030 Therm"""

# In [127]: dict(x.split() for x in strs.splitlines())
# Out[127]: {'A1023': 'CRT', 'A1029': 'Regulator', 'A1030': 'Therm'}
        

