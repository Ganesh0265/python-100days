rows=input("Enter the number of rows:")
if not rows.isdigit():
    print("Invalid Input!")
else:
    rows=int(rows)
    for i in range(rows):
        print(" "*(rows-i-1)+"*"*(2*i+1))