#program to check if the number is palindrome or not
#later I converted the program into loop
num=int(input("Enter any number:"))

for i in range(1,num+1):
  original=i #the value of num will change later so store it in another variable
  reverse=0 

  while i>0:
     digit=i%10  #the remainder is the last number 
     reverse=reverse*10+digit #the number will be added in reverse order each time
     i=i//10 #divides the num to the nearest whole number

  if original==reverse:
    print(original)
