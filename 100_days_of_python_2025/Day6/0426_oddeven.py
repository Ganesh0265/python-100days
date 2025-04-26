num=input("Enter any number:")
if not num.isdigit():
    print("Invalid Input!")
else:
    num=int(num)
    if num%2 == 0:
        print("The number is even.")
    else:
        print("The number is odd.")