# Crate a program that draws a chess table like this
#
# % % % % 
#  % % % %
# % % % %
#  % % % %
# % % % %
#  % % % %
# % % % % 
#  % % % %
#

num = int(input("Please provide a number!"))

odd = "% % % %"
even = " % % % %"

for i in range(num):
    print (odd)
    print (even)