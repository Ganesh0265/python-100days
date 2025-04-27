#This is a simple code to represent use of loop for recursion to print fibonacci series.
#This also uses the concept of swapping values between variables in python.

num=int(input("Enter upto how many terms you want to continue:"))
a,b=0,1 #in fibonacci 0 and 1 keep on adding next number on right to create another number.
for i in range(1,num+1):
    print(a)
    a,b=b,a+b  #You can swap value or modify the swapped value of variables in following ways.
