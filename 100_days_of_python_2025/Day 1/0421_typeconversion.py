a=123
b="Ram"
c="456"

# here the variable a is storing numeric data while the data stored in c is string 
#we can convert the data type in following way

print(type(int(c)))#this is the type of data in variable c which is string

print(str(a)+c+"and"+b)#here variable a is converted into string from integer
print(a+int(c)) #here variable c is converted into integer data type as int(c)