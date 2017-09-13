# Write a program that reads a number from the standard input, then draws a
# square like this:
#
#
# %%%%%
# %%  %
# % % %
# %  %%
# %   %
# %%%%%
#
# The square should have as many lines as the number was

# if num % 2 == 1:
#     between = ("%" + ((num-2)//2)* " "+ "%" + ((num-2)//2)* " " +"%")
# elif num % 2 == 0:
#     between = ("%" + ((num-2)//2)* " "+ "%" + ((num-2)//2-1)* " " +"%")

num = int(input("Please provide a number!"))

envelope = num * "%"
   
if num <= 2:
    for i in range(num):
        print (envelope)
    
elif num > 2:
    print (envelope)
    for i in range(num-2):
        between = ("%" + i * " " + "%" + (num-3-i)* " " +"%")
        print (between) 
    print (envelope)