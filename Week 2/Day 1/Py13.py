current_hours = 14;
current_minutes = 34;
current_seconds = 42;

# Write a program that prints the remaining seconds (as an integer) from a
# day if the current time is represented bt the variables

day_seconds = 24*60*60
print ("There is " + str(day_seconds) + " seconds in a day.")

past_time = (current_hours*60*60+current_minutes*60+current_seconds)
print ("Today " + str(past_time) + " seconds has already past.")

remaining_time = (day_seconds - past_time)
print ("There is still " + str(remaining_time) + " seconds left of today." )