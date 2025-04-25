#this is the beginner friendly code for previous days program to check age group

age=input("Enter your age: ")

if not age.isdigit(): #isdigit function can only be used for string digits
    print("Invalid Input!")
else:#if the string is digit then only this block will be executed
    age=int(age)#then you have to convert str type into int type for comparision
    if age > 0 and age < 12:
        print("You are a child.")
    elif age >= 12 and age < 20:
        print("You are a teenager.")
    elif age >= 20 and age < 45:
        print("You are an adult.")
    elif age >= 45 and age < 102:
        print("You are old.")
    else:
        print("What a beautiful lie, now you must die...")