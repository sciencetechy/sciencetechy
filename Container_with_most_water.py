"""You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store."""

height = [1,8,6,2,5,4,8,3,7] # example
b = False
st = 0
en = len(height)-1
biggest = 0

while not b:
    line1 = height[st]
    line2 = height[en]

    if biggest < (en-st)*min(line1, line2):
        biggest = (en-st)*min(line1, line2)

    if st == en-1:
        b = True
    
    if min(line1, line2) == line1:
        st += 1
    elif min(line1, line2) == line2:
        en -= 1
    elif line1 == line2:
        if height[st+1] > height[en-1]:
            st += 1
        else:
            en -= 1
    
print(biggest)