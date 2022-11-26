"""

Problem Specification:

CCC Problem D: When in Rome
If the Roman Empire had not fallen, then Rome would surely have discovered electricity and used electronic calculators; however, the Romans used Roman
Numerals! Your task is to implement a simple Roman Calculator which accepts two Roman Numerals and outputs the sum in Roman Numerals.
You may assume that numbers greater than 1000 will not occur in the input. Output numbers greater than 1000 are illegal and should generate the message CONCORDIA CUM VERITATE
(In Harmony with Truth).

Algorithm:
The Roman Numerals used by the Romans evolved over many years, and so there are some variations in the way they are written. We will use the following definitions:

The following symbols are used: I for 1, V for 5, X for 10, L for 50, C for 100, D for 500, and M for 1000.
Numbers are formed by writing symbols from 1. from left to right, as a sum, each time using the symbol for the largest possible value. The symbols M, C, X, or I may be used at most three times in succession. Only if this rule would be violated, you can use the following rule:
When a single I immediately precedes a V or X, it is subtracted. When a single X immediately precedes an L or C, it is subtracted. When a single C immediately precedes a D or M, it is subtracted.
For example: II = 2; IX = 9; CXIII = 113; LIV = 54; XXXVIII = 38; XCIX = 99.

Input Specification:

The input consists of a number, indicating the number of test cases, followed by this many test cases.
Each test case consists of a single line with two numbers in Roman Numerals separated by a + along with an = at the end. There are no separating spaces.

Output Specification:
For each test case the output is a copy of the input with the Roman Numeral that represents the sum.
Outputs for different test cases are separated by a blank line.

"""





def repeat_check(i):

    roman = i.split('+')
    a = roman[0]
    b = roman[1]

    for u in roman:
        if (u.find('iiii') != -1) or (u.find('xxxx') != -1) or (u.find('cccc') != -1) or (u.find('ll') != -1) or (u.find('vv') != -1) or (u.find('dd') != -1) or (u.find('vx') != -1):
            return("CONCORDIA CUM VERITATE")
        
   
    if a.find("cm"):
        a = a.replace("cm", "f")

    if a.find("cd"):          
        a = a.replace("cd", "e")

    if a.find("xc"):
        a = a.replace("xc", "d")

    if a.find("xl"):          
        a = a.replace("xl", "c")

    if a.find("ix"):
        a = a.replace("ix", "9")

    if a.find("iv"):          
        a = a.replace("iv", "4")


    if b.find("ix"):
        b = b.replace("ix", "9")

    if b.find("iv"):          
        b = b.replace("iv", "4")
    
    roman[0] = a
    roman[1] = b
        
    

    return(roman)

def find_dig(a):

    if a == "m":
        return(1000)

    if a == "d":
        return(500)

    if a == "c":
        return(100)
            
    if a == "l":
        return(50)
   
    if a == "x":
        return(10)
    
    if a == "v":
        return(5)

    if a == "i":
        return(1)

    if a == "9":
        return(9)
            
    if a == "4":
        return(4)

    if a == "c":
        return(40)
    
    if a == "d":
        return(90)
    
    if a == "e":
        return(400)
    
    if a == "f":
        return(900)


def find_val(rom):

    b = rom
    val = 0
    Last_dig = 0

    if len(rom) == 1:
        val = (find_dig(rom))

    for x in range(1, len(rom)):

        Current_dig = rom[x]
        Last_dig = rom[x-1]

        if type(Current_dig) == str:
            Current_dig = find_dig(Current_dig)

        if type(Last_dig) == str:
            Last_dig = find_dig(Last_dig)

        if val > 0:
            Last_dig = val

        if Current_dig > Last_dig:
            val = Current_dig - Last_dig
        
        elif Current_dig < Last_dig or Current_dig == Last_dig:
            val = Last_dig + Current_dig
        
    return(val)


def rom_val(dec):

    low = 0
    high = 0

    if dec == 1:
        return("i")
    
    if dec == 5:
        return("v")
    
    if dec == 10:
        return("x")

    if dec == 50:
        return("l")

    if dec == 100:
        return("c")

    if dec == 500:
        return("d")

    if dec == 1000:
        return("m")

    if dec > 1 and dec < 5:
        low = 1
        high = 5
    
    elif dec > 5 and dec < 10:
        low = 5
        high = 10

    elif dec > 10 and dec < 50:
        low = 10
        high = 50

    elif dec > 50 and dec < 100:
        low = 50
        high = 100

    elif dec > 100 and dec < 500:
        low = 100
        high = 500

    elif dec > 500 and dec < 1000:
        low = 500
        high = 1000
    
    if high - dec == 1 or high - dec == 5 or high - dec == 10 or high - dec == 50 or high - dec == 100 or high - dec == 500 or high - dec == 1000:
        return(rom_val(high - dec) + rom_val(high))
    else:    
        return(rom_val(low) + rom_val(dec - low))


num = int(input(""))

for i in range(0, num):
    inp_str = input("")

    if inp_str.find("=") != 1:
        inp_str = inp_str.replace("=", "")

    roman = repeat_check(inp_str)

    first_rom = find_val(roman[0])
    second_rom = find_val(roman[1])

    tot_val = first_rom + second_rom

    if tot_val > 1000:
        print("CONCORDIA CUM VERITATE")
        quit()

    tot_rom = rom_val(tot_val)

    print(tot_rom)