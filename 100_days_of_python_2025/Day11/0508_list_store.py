# last session's work
# This code is used to store list with user details inside another list.

total_list=[]

for i in range(1,6):
    temp_list=[]
    name=input("Enter your name:")
    mobile_number=input("Enter your mobile number:")
    address=input("Enter your address:")
    temp_list.append(name)
    temp_list.append(mobile_number)
    temp_list.append(address)
    total_list.append(temp_list)
print(total_list)