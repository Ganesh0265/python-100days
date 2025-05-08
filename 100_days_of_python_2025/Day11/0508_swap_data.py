#This code is to demonstrate swapping data of two variable.
a=5
b=9

print("The value of \"a\" before swap :",a)
print("The value of \"b\" before swap :",b)
#to swap the data in basic way we can create a temporary variable to store one data first like
c=a #this is the temporary variable that will store value of a 
a=b #the value in variable a is changed now it contains value of b
b=c #the value in variable b is changed now it contains value of c which was the initial value of a

print("The value of \"a\" after swap :",a)
print("The value of \"b\" after swap :",b)

#this one used the optimum method of data swap in python

a,b=b,a # this way you can swap the value of two varibles without need for temporary variable

print("The value of \"a\" with direct swap :",a)
print("The value of \"b\" with direct swap :",b)