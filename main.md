import random
choice=["rock","paper","scissor"]
user_choice=input(("Enter youy choice (Rock,Paper,scissor):"))
user=user_choice.lower()
computer_choice=random.choice(choice)
print("computer choice: ",computer_choice)
print("User choice: ",user_choice)

if user==computer_choice:
    print("It is a tie")
elif user=="rock" and computer_choice=="scissor":
    print("Stone smashes scissor ,You win!")
elif user=="paper" and computer_choice=="rock":
    print("Paper can cover rock , You ! win")
elif user=="scissor" and computer_choice=="paper":
    print("Scissor can cut paper You win")
else:
    print("Computer won")
