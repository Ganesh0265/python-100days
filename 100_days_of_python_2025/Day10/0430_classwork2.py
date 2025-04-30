#This code is to store name, contact number and address of 5 friends in a list. i.e. store list inside list.

total_data=[]
for i in range(1,6):
    list1=[]
    print(f"This is the detail of friend number {i}")
    name=input("Enter your name:")
    contact=input("Enter your phone number:")
    address=input("Enterr your address:")
    list1.append(name)
    list1.append(contact)
    list1.append(address)
    total_data.append(list1)
print(total_data)