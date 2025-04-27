#This code shows the way to use while loop 
#This code is the basic demonstration of syntax of while loop

condition=True
count=0
while condition:
    print(f"This is condition number {count+1}")
    if count==4:
        condition=False
    count=count+1
print("Now the loop must stop as the only first fifth condition is True")

i=1
while i<=100:
    print(i)
    i=i+1
