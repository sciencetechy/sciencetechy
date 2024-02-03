"""
Problem Description
You have to determine if it is possible to escape from a room. The room is an M-by-N grid with
each position (cell) containing a positive integer. The rows are numbered 1, 2, . . . , M and the
columns are numbered 1, 2, . . . , N. We use (r, c) to refer to the cell in row r and column c.
You start in the top-left corner at (1, 1) and exit from the bottom-right corner at (M, N). If you
are in a cell containing the value x, then you can jump to any cell (a, b) satisfying a × b = x. For
example, if you are in a cell containing a 6, you can jump to cell (2, 3).
Note that from a cell containing a 6, there are up to four cells you can jump to: (2, 3), (3, 2), (1, 6),
or (6, 1). If the room is a 5-by-6 grid, there isn’t a row 6 so only the first three jumps would be
possible.

Input Specification
The first line of the input will be an integer M (1 ≤ M ≤ 1000). The second line of the input will
be an integer N (1 ≤ N ≤ 1000). The remaining input gives the positive integers in the cells of
the room with M rows and N columns. It consists of M lines where each line contains N positive
integers, each less than or equal to 1 000 000, separated by single spaces.

Output Specification
Output yes if it is possible to escape from the room. Otherwise, output no.
"""
def possible_func(table, point, r):
    possible = False
    contain = None
    row_index = 0
    coloumn_index = 0
    escaped = False

    while not escaped:
        for row in table:
            row_index += 1
            if row_index > r:
                row_index = 1

            if point in row:
                contain = True
                h = row.count(point)
                if h > 1:
                    indices = [i for i in range(len(row)) if row[i] == point]
                    h = 0
                    for k in indices:
                        escaped = possible_func(table, (k+1)*row_index, r)
                        if escaped == True:
                            return True

                else:
                    if point == table[0][0]:
                        escaped = True
                        possible = True
                        return possible
                    else:
                        coloumn_index = row.index(point)+1
                        point = row_index*coloumn_index
            
            

        if contain == False:
            escaped = True
            possible = False
    
    return possible
    
# input
r = int(input(""))
c = int(input(""))
table = []
escaped = False
exit = r*c
point = exit
possible = False
row_index = 0
coloumn_index = 0
contain = False

for i in range(r):
    cl = input("")
    y = cl.split(' ')
    ru = []
    for i in y:
        t = int(i)
        ru.append(t)

    table.append(ru)


possible = possible_func(table, point, r)
        
        


if possible:
    print('yes')
elif not possible:
    print('no')