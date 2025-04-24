#program to check if the number is prime or not
import math #It is needed to use square root function
num=int(input("Enter any number:"))

if num<=1:
     print("It is not a prime number.")
elif num==2:
     print("It is prime number.")
else:
    is_prime=True
    for i in range(2,int(math.sqrt(num))+1): #You don't have to divide the number from 2 to num, instead you can do upto sqrt of n plus 1
      if num%i==0: #if it is divisible than it is not a prime number
          is_prime=False
    if is_prime:
         print("The number is Prime.")
    else: 
        print("The number is not Prime.")