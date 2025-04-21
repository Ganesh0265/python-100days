#WAP to add, sub, multiply and divide any two numbers.

# these are practice of operators in python
a=15
b=3

print("This is addition:", a+b)
print("This is subtraction:", a-b)
print("This is multiplication:", a*b)
print("This is division:", a/b)
print("This is division:", a//b) #this is integer division
print("This is division:", a%b) #this operator gives the remainder

#use of formatting in print : this later useful in may complex programs

print(f"This remainder after dividing {19} by {b} is: {19%b}")

#if we use (  end=","  ) after formatting string it will replace the end value of print with comma

print(f"This remainder after dividing {19} by {b} is: {19%b}",end=",")
print("This is the text which is in new line")