#This code is to revise the usage of loops which we studied before:
#Program to print the reverse of the input word
word=input("Enter any word:")
reverse=" "
for i in range(1,len(word)+1):
    reverse=reverse+word[-i]
print(f"The reverse of \"{word}\" is \"{reverse}\" ")


print("""


""")

#This code prints from 25 to 15 in backward order

for i in range(25,14,-1):
    if i==15:
        print(i)
    else:
        print(i,end=',')
