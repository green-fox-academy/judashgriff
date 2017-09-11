# An average Green Fox attendee codes 6 hours daily
# The semester is 17 weeks long
#
# Print how many hours is spent with coding in a semester by an attendee,
# if the attendee only codes on workdays.
#
# Print the percentage of the coding hours in the semester if the average
# work hours weekly is 52
work_hours = 17*5*6
average = 17*52

print (str(work_hours) + " hours of coding in total")

print ( str(work_hours % average * 100) + "%")

percentage = work_hours / average * 100 

print (str(percentage // 1) + "%")  
