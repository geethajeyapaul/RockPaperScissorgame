import random

# print multiline instruction
# performstring concatenation of string
print('Winning rules of the game ROCK PAPER SCISSORS are :\n'
      + "Rock vs Paper -> Paper wins \n"
      + "Rock vs Scissors -> Rock wins \n"
      + "Paper vs Scissors -> Scissor wins \n")

optionsforcomputer = ["Rock", "Paper", "Scissors"]

user_choice = input("Enter your option: Rock, Paper, or Scissors: ")

computer_choice = random.choice(optionsforcomputer)

print("You chose: ", user_choice)

print("Computer chose: ", computer_choice)

if user_choice == computer_choice:

    print("It's a tie!")

elif user_choice == "Rock" and computer_choice == "Scissors":

    print("You win!")

elif user_choice == "Paper" and computer_choice == "Rock":

    print("You win!")

elif user_choice == "Scissors" and computer_choice == "Paper":

    print("You win!")
