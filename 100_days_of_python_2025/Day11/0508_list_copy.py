#Implementation of copy method for list rather than putting memory addres of the other list.

#This example is by using memory address of first list in second list
list1=[1,2,3,4,5,6]
list2=list1 #storing memeory address of list1 in list2
j=0
for i in list1:
    list1[j]=i*i #operation only done in list1
    j+=1
print(list1)
print(list2) #list2 prints the same result as list1



print("-------------------------------------------------------")
print("Using copy method:")
list1=[1,2,3,4,5,6]
list2=list1.copy() #Now list2 stores data of list1 rather than the memory address
j=0
for i in list1:
    list1[j]=i*i
    j+=1
print(list1)
print(list2) #the data doesnot change as it is constant and not gone though any operation