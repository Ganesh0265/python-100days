countries=("Spain", "Italy", "India", "England", "Germany")

# you can only use methods of list on tuple by converting tuple into list

temp=list(countries)
temp.append("Russia")
temp.pop(3)
temp[2]="Finland"
countries=tuple(temp)
print(countries)

tuple1=(0,1,2,3,5,4,3,3,31)
res= list(tuple1)
print(tuple1.index(3))
print(tuple1.count(3))
res.append(4)
print(res)