# - Create (dynamically) a two dimensional list
#   with the following matrix. Use a loop!
#
#   1 0 0 0
#   0 1 0 0
#   0 0 1 0
#   0 0 0 1
#
# - Print this two dimensional list to the output

matrix = [[],[],[],[]]
for i in range(len(matrix)):
    matrix[i] = [0,0,0,0]
    matrix[i][i]+=1

for n in matrix:
    print(n)