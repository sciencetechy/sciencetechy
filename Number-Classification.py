"""
CCC 2022 Problem J3: Harp Tuning
Problem Description:

Problem Specification:
Write a program that repeatedly reads a positive integer, determines if the integer is deficient, perfect, or abundant
and outputs the number along with its classification.

A positive integer, n, is said to be perfect if the sum of its proper divisors equals the number itself.

(Proper divisors include 1 but not the number itself.) If this sum is less that n, the number is deficient, and if the sum is greater than n, the number is abundant.

Input Specification:

The input starts with the number of integers that follow. You may assume that the input integers are greater than 1 and less than 32500.


Output Specification:

For each of the input integers, classify each number as deficient, abundant and perfect.

"""


import math

# inputs, list and variables

amt_num = int(input("How many nums do you want to input?"))
list_of_nums = []

# all numbers added

for i in range(1, amt_num+1):
    num = int(input("what num?"))
    list_of_nums.append(num)

# finding what each number is classified as

for num in list_of_nums:
   a = 0
   factors = []

   y = math.ceil(num/2)

   for x in range(1, y+1):
        if num % x == 0:
            factors.append(x)
    
   for x in factors:
        a += x

   if a == num:
      print(num, "is a perfect number.")
   elif a > num:
      print(num, "is a abundant number.")
   elif a < num:
      print(num, "is a deficient number.")