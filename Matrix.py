import random, os
os.system("cls")

matrix = []
row = int(input("Enter Row No.:\t\t"))
column = int(input("Enter Column No.:\t"))
print("")

for i in range(row):
    innermatrix = []

    print("For {} Row.".format(i+1).center(40,"-"))
    print("")
    for j in range(column):
        rip = int(input("Enter value for [{}][{}]:\t".format(i+1,j+1)))
        innermatrix.append(rip)
    matrix.append(innermatrix)
    print("")
print("\nYour {} x {} Matrix is:".format(row,column))

for i in range(row):
    for j in range(column):
        if(j == (column-1)):
            print("{} ".format(matrix[i][j]), end=" ")
        else:
            print("{} |".format(matrix[i][j]), end=" ")
    print("")
print("\n")


