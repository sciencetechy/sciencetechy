"""

Problem Description:

A new and up coming artist has a unique way to create checkered patterns.
The idea is to use an M-by-N canvas which is initially entirely black.
Then the artist repeatedly chooses a row or column and runs their magic brush along the row or column.
The brush changes the colour of each cell in the row or column from black to gold or gold to black. 
Given the artist choices ,your job is to determine how much gold appears in the pattern determined by these choices.


Input Specification:

The first line of input will be a positive integer M. The second line of input will be a positive integer N.
The third line of input will be a positive integer K. The remaining input will be K lines giving the choices made by the artist.
Each of these lines will either be R followed by a single space and then an integer which is a row or a Coloumn followed by a single 
space and then an integer which is a column number. Rows are numbered top down from 1 to M. Columns are numbered left to right from 1 to N.

Output Specification:

Output one non-negative integer which is equal to the number of cells that are gold in the pattern determined by the artists choices
"""



def gr_make(row, col):
    arr = []

    for j in range (0, row):
        new = []

        for i in range (0, col):
            new.append(0)

        arr.append(new)
    
    return arr

def change(arr, lis, u):
    p = lis[u]
    num = int(p[2])
    ltr = p[0]

    if ltr == 'r' or ltr == 'R':
        ar = ro(arr, num)

    elif ltr == 'c' or ltr == 'C':
        ar = co(arr, num)
    
    return(ar)

def ro(ar, num):

    num -= 1

    t = ar[num]
    u = len(t)
    for i in range(0, u):
        if t[i] == 0:
            t[i] = 1
        else:
            t[i] = 0
    
    return(ar)

def co(ar, num):
    v = len(ar)

    for i in range(0, v):
        if ar[i][0] == 0:
            ar[i][0] = 1
        else:
            ar[i][0] = 0
    
    return(ar)

row = int(input(' '))
col = int(input(' '))
num = int(input(' '))

ro_col = []

for i in range(0, num):
    r = str(input(' '))
    ro_col.append(r)

t = len(ro_col)

g = gr_make(row, col)

for x in range(0, t):
    r = change(g, ro_col, x)
    g = r

y = len(g)
ct = 0

for i in range(0, row):
    for x in range(0, col):
        if g[i][x] == 1:
            ct += 1

print(ct)