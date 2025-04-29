#This code is to show how to create pattern like:
#*
#**
#***
#****
#*****
design=input("Enter which symbol do you want to use for pattern:")
times=input("For how many times do you want to repeat:")
if not times.isdigit():
    print("Invalid Input!")
else:
    times=int(times)
    last=" "
    for des in range(1,times+1):
        last=last+design

    for i in range(0,times+1):
        for j in range(1):
            if i>=j:
                print(last[1:i+1])
