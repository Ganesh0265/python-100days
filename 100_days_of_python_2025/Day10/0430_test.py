#This code is to represent a simple password generator with combination of strings.
string=input("Enter any string upto 4 letters:")
for i1 in string:
    print(i1)
    for i2 in string:
        if(i1==i2):
            continue
        else:
            print(i1,i2)
        for i3 in string:
            if i1==i2 or i2==i3 or i1==i3:
                continue
            else:

                print(i1,i2,i3)
            for i4 in string:
                if i1==i2 or i2==i3 or i3==i4 or i1==i3 or i2==i4 or i1==i4:
                    continue
                else:
                    print(i1,i2,i3,i4)