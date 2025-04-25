answer=73
count=10
print("Guess The Number!")

for i in range(1,11):
    print(f"You have {count-i} chances to guess the correct number!")
    number=input("Enter any number:")

    if not number.isdigit():
        print("Invalid Input!")
        
    else:
        number=int(number)
        if number==answer:
            print("Congratulations! You have guessed correct number!")
            break
        else:
            if number>0 and number<=56:
                print("The number is too much less.")
            elif number>56 and number<=65:
                print("Guess a little higher!")
            elif number>65 and number<=72:
                print("You were very close to it!")
            elif number>73 and number<=80:
                print("You guessed a little bit more.")
            elif number>80 and number<=100:
                print("That is too high. Try again")
            else:
                print("Invalid input!")