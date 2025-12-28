import random 
play=True
number=str(random.randint(10,20))
print("Lets guess the number between 10 and 20")
print("The game will end when you guess the correct number")

while play:
    guess=input("Enter your guess number: ")
    if number == guess:
        print("You guessed it right ")
        print("The number is ",number)
        break
    else:
        print("Wrong guess try again")
