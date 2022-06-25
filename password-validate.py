# Write a Python program to check the validity of password input by users:

# At least 1 letter between [a-z] and 1 letter between [A-Z].
# At least 1 number between [0-9].
# Minimum length 6 characters.
# Maximum length 16 characters.


from curses.ascii import isalpha

pas = input("Which password would you like to put in?")
count_let = 0
count_num = 0

# checking to make sure the password is not lesser than 6 letters and not greater than 16
if len(pas) < 6:
  print(" Invalid Password, Password must be more than 6 letters long ")
elif len(pas) > 16:
  print(" Invalid Password, Password must be less than 16 letters long ")

# checking for uppercase using the lowercase function
if pas.islower() == True:
  print(" Invalid Password, Password must have at least one uppercase letter")

# checking for lowercase using the uppercase function
if pas.isupper() == True:
  print(" Invalid Password, Password must have at least one lowercase letter")

# checking for a num
if pas.isalnum() == False:
  print("Invalid password, password needs at least one number")