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

#this code prints if it is odd and even beside the number upto 50
i=1
while i<=50:
    if i%2==0:
        print(f"{i}(Even)")
    else: 
        print(f"{i}(Odd)")
    i=i+1
