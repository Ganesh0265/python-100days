#This code is to demonstrate the use of for loop in list data types(data structure).
animals=['elephant','lion','tiger','ape','rabbit','cat','dog']
for animal in animals:
    if animal[0] in "aeiou":
        article="an "
    else:
        article="a "
    sentence="It is "+article+animal+"."
    print(sentence)