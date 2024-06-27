"""You are given an integer array arr of length n that represents a permutation of the integers in the range [0, n - 1].

We split arr into some number of chunks (i.e., partitions), and individually sort each chunk. After concatenating them, the result should equal the sorted array.

Return the largest number of chunks we can make to sort the array."""


arr = [4,3,2,1,0] # example
norm = arr.copy()
arr.sort()
intv = {}

for i in range(len(arr)):
    intv[norm[i]] = [i]

for i in range(len(arr)):
    p = intv[arr[i]]
    p.append(i)
    intv[arr[i]] = p


t = list(intv.values())
t.sort()
stack = []

for i in t:
    if not stack:
        stack.append(i)
    else:
        prev = stack.pop()
        if prev[1] >= i[0]:
            if prev[1] <= i[1]:
                prev = [prev[0], i[1]]

            stack.append(prev)
        else:
            stack.append(prev)
            stack.append(i)

print(len(stack))