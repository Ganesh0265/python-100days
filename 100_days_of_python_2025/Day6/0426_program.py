#This code is to show the use of condition using if elif else statement.
name=input("Enter Your Name:")
marks=input("Enter Your Percentage:")

if not marks.isdigit():
    print("Invalid Input!")
else:
    marks=int(marks)
    if marks>0 and marks<=34:
        print(f"Your result is not good.")
        print("You got F")
    elif marks>=35 and marks<40:
        print(f"You have to work harder {name}.")
        print("You got D")
    elif marks>=40 and marks<=49:
        print(f"Be laborious.")
        print("You got C")
    elif marks>=50 and marks<=59:
        print(f"Your result is Satisfactory.")
        print("You got C+")
    elif marks>=60 and marks<=69:
        print("Your result is Good.")
        print("You got B")
    elif marks>=70 and marks<=79:
        print(f"Your result is Very-Good.")
        print("You got B+")
    elif marks>=80 and marks<=89:
        print(f"Your result is Excellent.")
        print("You got A")
    elif marks>=90 and marks<=100:
        print(f"Your result is Outstanding.")
        print("You got A+")
    else:
        print("Please enter correct marks!")