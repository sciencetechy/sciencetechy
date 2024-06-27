"""You are given a 2D binary array grid. Find a rectangle with horizontal and vertical sides with the smallest area, such that all the 1's in grid lie inside this rectangle.

Return the minimum possible area of the rectangle."""


grid = [[0,1,0],[1,0,1]] # example
possible = True
ones = []

for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == 1:
            ones.append([i,j])


if len(ones)!=1:
    h1 = ones[0][0]
    w1 = ones[0][1]
    h2 = ones[0][0]
    w2 = ones[0][1]

    for i in ones:
        h1 = max(i[0], h1)
        h2 = min(i[0], h2)
        w1 = max(i[1], w1)
        w2 = min(i[1], w2)


    print((h1-h2+1)*(w1-w2+1))

else:
    print(1)