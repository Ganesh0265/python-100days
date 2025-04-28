#This code is to demostrate for loop for string data types.
a="SAGARMATHA"
count=1
for i in a:
    print(f"The current letter is {i}")
print("""



""")
#This code is to count how many words are there is the entered sentence.
sentence=input("Write a sentence:")
count=1
for i in sentence:
    if i==" ":
        count=count+1
print(f"There are {count} words in the sentence")
