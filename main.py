import pycosat
import time
start=time.time()

def findval(i,j,num):        #finding a particular variable for defining the particular stae of a cell
    return 100*i + 10*j + num
list1 = []

# Each cell in puzzle contains at least one value
for i in range(9):
    for j in range(9):
        temp = []
        for num in range(1,10):
            temp.append(findval(i,j,num))
        list1.append(temp)

# Each cell in the puzzle contains at most one value
for i in range(9):
    for j in range(9):
        for x in range(1,10):
            for y in range(x+1,10):
                list1.append([-(findval(i,j,x)) , -(findval(i,j,y))])

# Each row in the puzzle should contain all the values.
for i in range(9):
    for num in range(1,10):
        temp = []
        for j in range(9):
            temp.append(findval(i,j,num))
        list1.append(temp)

# Each column in the puzzle should contain all the values.
for j in range(9):
    for num in range(1,10):
        temp = []
        for i in range(9):
            temp.append(findval(i,j,num))
        list1.append(temp)

# Each smaller block should contain all the values.
tempi = 0
tempj = 0
i = 3
j = 3
while i<=9 and j<=9:
    for num in range(1,10):
        temp = []
        for x in range(tempi , i):
            for y in range(tempj,j):
                temp.append(findval(x,y,num))
        list1.append(temp)
    if i<9:
        tempi = i
        i+=3
    else:
        tempi = 0
        i = 3
        tempj = j
        j+=3

# The initial setup (values for some of the cells) and solving it
size = len(list1)
f = open("p.txt","r")          # opening file in read mode only to read soduko
g = open("ans.txt","w")        # opening file in write mode only to write the solutions
lines = f.readlines()
for line in lines:
    line = line[:-1]
    for i in range(len(line)):
        if (line[i]!="."):
            #decoding the variable 
            row_num = i//9
            col_num = i%9
            num = int(line[i])
            list1.append([findval(row_num,col_num,num)])

    cnf = pycosat.solve(list1)
    if cnf == "UNSAT":
        print("the clauses are unsatisfiable")
    elif cnf == "UNKNOWN":
        print("a solution could not be determined within the propagation limit")
    else:
        s = ""
        for i in cnf:
            if i > 0:
                s += str(i%10)
        s += "\n"
        g.write(s)
        list1 = list1[:size]
end = time.time()
print("Time: ",end-start)

        