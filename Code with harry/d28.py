# This code shows normal string formatting with values from variables.
letter="Hey my name is {} and I am from {}"
country="Nepal"
name="Ganesh"
print(letter.format(name, country))

#now using f-strings
print(f"This is a f-string made by {name} form {country}")

# another example
price=123.456
txt=f"For only {price:.2f} dollars"
print(txt)