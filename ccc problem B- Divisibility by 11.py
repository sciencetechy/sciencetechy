"""
CCC Problem B: Divisibility by 11

Problem Specification:
Write a program which accepts as input a positive integer and checks, using the algorithm described below, to see whether or not the integer is divisible by 11.

Algorithm:
As long as the number being tested has more than two digits, form a new number by:
deleting the units digit
subtracting the deleted digit from the shortened number
The remaining number is divisible by 11 if and only if the original number is divisible by 11.

Input Specification:
As usual, the first number in the input indicates the number of positive integers that follow. Each positive integer has a maximum of 50 digits.
You may assume no leading zeroes exist in the positive integers.

Output Specification:
For each positive integer in the input, the output consists of a series of numbers formed as a digit is deleted and subtracted,
followed by a message indicating whether or not the original number is divisible by 11. Outputs for different positive integers are separated by blank lines.

"""

length = 0
x = int(input("what num?"))
l = x
c = 1
u = 0
r = x

while c > 0:
    
    length += 1

    u = l // 10
    l = l // 10

    if u == 0:
        c -= 1



for i in range(length+2, 0, -1):

    val = x%10

    if val == 0:
        x = x // 10

    else:
        x = x // 10
        x -= val

    print(x)

    if x == 11:
        print(r, "is divisible by 11")
        break

    elif x < 21:
        print(r, "is not divisible by 11")
        break

    elif x < 11:
        break
