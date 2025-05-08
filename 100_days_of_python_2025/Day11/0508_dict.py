new_dict={'name':'Ganesh','mobile no.':'980000000','address':'Bharatpur'}
print(new_dict)
print(new_dict.keys())
print(new_dict.values())
print(new_dict.items())
print(new_dict['name'])
print(new_dict['address'])

for key in new_dict:
    if key=='mobile no.':
        print(new_dict[key])
        