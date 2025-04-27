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
print("""


""")
#now this code prints prime number upto 50 using while loop
j=0
while j<=50:
    if j==0 or j==1:
        print(f"{j} is not a prime number.")
    elif j==2:
        print(f"{j}(Prime)")
    if j>2:
        k=2
        count=0
        while k<=j:
            if j%k==0:
              count=count+1  
            k=k+1
        if count>=2:
            print(f"{j}(Composite)")
        else:
            print(f"{j}(Prime)")
    j=j+1


#I made this code work after 5 modifications ( T-T) .