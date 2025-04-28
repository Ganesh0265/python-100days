#This code shows how to reverese a string using loop
name="HKASIAB"
reverse=""
for i in range(1,len(name)+1):
    reverse=reverse+name[-i]
print(f"The reversed word is {reverse}")