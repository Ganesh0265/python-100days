#types of condition
# if, if ...else, if ...elif ...else (nested condition)

age=int(input("Enter Your Age:"))
if age>=18:
     print("You can vote!")
else:
     print("You cannot vote!")


#write a program to find if the user is child, teenager, adult or old
age1=int(input("Enter Your Age:"))

if age1>0 and age1<12:
     print("You are a child.")
elif age1>=12 and age1<20:
     print("You are a teenager.")
elif age1>=20 and age1<45:
     print("You are an adult.")
elif age1>=45 and age1<102:
     print("You are Old.")
else:
     print("What a beautiful lie, now you must die...")
