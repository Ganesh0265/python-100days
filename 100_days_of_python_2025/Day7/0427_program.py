#As I am revising all of the python fundamentals 
#today I am relearning about loops
#The loop statements that I'm going to learn is 
#for loop
#while loop

#program to print prime numbers from the entered range of number starting from one
import math
num=input("Enter the range of number:")
if not num.isdigit():
    print("Invalid Input!")
else:
    num=int(num)
    
    for i in range(1,num+1):
        if i==0 or i==1:
            pass
        if i==2:
            print(i)
        if i%2==0:
           pass
        if i>2:
            is_prime=True
            for j in range(2,int(math.sqrt(i)+1)):
                if i%j==0:
                    is_prime=False
            if is_prime:
                print(i)
        else:
            pass   
    