marks=input("Enter Your Percentage:")
if not marks.isdigit():
    print("Invalid Input!")
else:
    marks=int(marks)
    if marks>0 and marks<=34:
        print("You got F")
    elif marks>=35 and marks<40:
        print("You got D")
    elif marks>=40 and marks<=49:
        print("You got C")
    elif marks>=50 and marks<=59:
        print("You got C+")
    elif marks>=60 and marks<=69:
        print("You got B")
    elif marks>=70 and marks<=79:
        print("You got B+")
    elif marks>=80 and marks<=89:
        print("You got A")
    elif marks>=90 and marks<=100:
        print("You got A+")