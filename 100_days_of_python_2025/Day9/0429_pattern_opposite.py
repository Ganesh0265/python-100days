#This code is copied from my previous program pattern.py and made some modifications.
#pattern:
# *****
# ****
# ***
# **
#*

design = input("Enter which symbol you want to use for pattern: ")
times = input("For how many times do you want to repeat: ")

if not times.isdigit():
    print("Invalid Input!")
else:
    times = int(times)
    for i in range(times, 0, -1):
        print(design * i)