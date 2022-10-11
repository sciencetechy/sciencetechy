"""
 Over All Problem:

   Write a program that repeatedly reads two numbers n and k and prints all bit patterns of length n with k ones in descending order (when the bit
 patterns are considered as binary numbers). 

 Input Specification:

   You may assume that 30 >= n > 0, 8 > k >= 0, and n >= k. The first number in the input gives the
 number of pairs n and k. 
 
 Output Specification:

   The numbers n and k are separated by a single space. Leading zeroes in a bit pattern should be included. See the example 
    below.
"""

import math

def verify_input(a, b):
    
    if a > 30 or a < 0:
        exit()
    if 8 < b or b < 0:
        exit()
    if a < b:
        exit()

def check_ones(v):

    tot_num = 0
    while v >= 1:

        if v % 2 == 1:
            tot_num += 1
        
        v = v // 2

    return(tot_num)


def check_len(i):

    x = bin(i)

    x = x.replace("0b", "")


    if len(x) < n:
        while len(x) < n:
            x = "".join(("0", x)) 

    return(x)        




y = 0
x = int(input(""))

for i in range(1,x+1):

    nk = input("")
    nk_split = nk.split(' ')
    n = int(nk_split[0])
    k = int(nk_split[1])
    verify_input(n, k)
    print("The bit patterns are")

    for r in range((n**2)-1, -1, -1):

        if check_ones(r) == k:
            print(check_len(r))