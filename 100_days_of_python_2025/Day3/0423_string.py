a="Ram"
b="Shyam"
c=9
sentence= "      this sentence has white space      "


print(a+str(c)) #the numeric data type is converted into string

print(len(a)) #It prints the length of characters in the string


print(sentence.strip()) #the strip command removes the white spaces

split_sentence= sentence.split(' ')
email="ganeshpariyar@gmail.com"
split_mail=email.split('@')

print(split_sentence)
print(split_mail)

#Replace string

another= "This is another sentence in which the word nepal is replaced"
replaced=another.replace('nepal','india')
print(replaced)

#Converting into uppercase and lowercase

name="alan turing"

print(name.upper()) #This converts all characters into uppercase
print(name.capitalize()) #This function capitalizes the first word in the string
print(name.title()) #This function capitalizes each words in the string

name= name.upper()
print(name) #now the text is in capital letters
print(name.lower()) #This function converts all characters into lowercase
