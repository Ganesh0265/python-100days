#Guessing number game modifired from day 5 with random number generation.
import random
answer=random.randint(1,100)
# answer=73
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
            if number<answer:
               print("Very Low!")
            else:
                print("Very High!")