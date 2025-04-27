#This code demostrates the basics of for loop 
#This code prints the multiplication table of entered number

num=input("Enter any number:")
if not num.isdigit():
    print("Invalid Input!")
else:
    num=int(num)
    for i in range(1,11):
        print(f"{num}X{i}={num*i}")