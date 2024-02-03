"""
Problem Description
Thuc likes finding cyclic shifts of strings. A cyclic shift of a string is obtained by moving characters
from the beginning of the string to the end of the string. We also consider a string to be a cyclic
shift of itself. For example, the cyclic shifts of ABCDE are:
ABCDE, BCDEA, CDEAB, DEABC, and EABCD.
Given some text, T, and a string, S, determine if T contains a cyclic shift of S.

Input Specification
The input will consist of exactly two lines containing only uppercase letters. The first line will be
the text T, and the second line will be the string S. Each line will contain at most 1000 characters.
For 6 of the 15 available marks, S will be exactly 3 characters in length.

Output Specification
Output yes if the text, T, contains a cyclic shift of the string, S. Otherwise, output no
"""
def find_combination(string):
    s = string
    comb = []
    l = list(s)
    t = ''

    for i in range(len(string)):
        first_element = l[0]
        l.pop(0)
        l.append(first_element)

        for i in l:
            t += i

        comb.append(t)
        t = ''
    
    return comb

org_text = input("")
str = input("")
all_combination = find_combination(str)
contain = False

for i in all_combination:
    if i in org_text:
        contain = True

if contain:
    print('Yes')
else:
    print('No')
        
    
