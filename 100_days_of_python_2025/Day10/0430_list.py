list1=["apple",99,"ball",99,"Ram","cat",1,"apple","ball"]
print(list1[1:4])
print(list1[::-1])

list2=[]

for i in list1:
    if i in list2:
        pass #I used continue first here but it will not run remaining parts so i used pass which will do nothing if there is same value.
    
    else:    
        list2.append(i)
        
print(list2)