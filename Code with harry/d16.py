# this code is about match case statements
x=int(input("Enter any Number:"))
match x:
    case 1:
        print("Thank You for visiting!")
    case 2:
        print("What the duck!")
    case 3:
        print("This is the last option")
    case _:
        print(x)
