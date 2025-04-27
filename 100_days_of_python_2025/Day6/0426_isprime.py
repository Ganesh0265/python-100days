import math
num=input("Enter any number:")
if not num.isdigit():
    print("Invalid Input!")
else:
    num=int(num)
    if num==0 or num==1:
        print("It is not a prime number.")
    if num==2:
        print("It is prime number.")
    if num%2==0:                     #this is just for code optimization for faster checking
        print("Is is composite number.")
    else:
        is_prime=True
        for i in range(2,int(math.sqrt(num))+1):
            if num%i==0:
                is_prime=False
        if is_prime:
            print("It is prime number.")
        else:
            print("It is composite number.")