#revising the use of range function from basic.

num=50
for i in range(50,0,-1):
    print(i)

print("""

This code prints even number from 1 upto the input number.

""")

value=input("Enter any number:")
if not value.isdigit():
    print("Invalid Input!")
else:
    value=int(value)
    for i in range(1,value+1):
        if i%2==0:
            print(i)
            