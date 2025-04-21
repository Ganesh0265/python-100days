# this code shows the way to use dictionary
dic={"name":"Ganesh","address":"Bharatpur-2","Ph.No.":"9816226758"}
print(dic)
print(dic["address"])
print(dic.get("name"))
print(dic.get("name2"))
print(dic.keys())
print(dic.values())
for key in dic.keys():
    print(dic[key])
for key in dic.keys():
    print(f"The value corresponding to {key} is {dic[key]}.")

#this shows another way for printing dictionary key and value by unpacking tuples
print(dic.items())
for key, value in dic.items():
    print(f"The value corresponding to the {key} is {value}")