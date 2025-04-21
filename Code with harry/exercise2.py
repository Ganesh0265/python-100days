# this code use time module to show and check system time
import time
timestamp= int(time.strftime('%H'))
print(timestamp)
if(timestamp in range(6,11)):
    print("Good Morning")
elif(timestamp in range(12,17)):
    print("Good Afternoon")
elif(timestamp in range(18,20)):
    print("Good Evening")
else:
    print("Good Night!")