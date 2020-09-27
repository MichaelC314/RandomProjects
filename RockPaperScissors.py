import random

while True:
    userInput = input("Enter the word quit to stop the game\nEnter Rock, Paper, or Scissors: ")

    if userInput.lower() == "rock" or userInput.lower() == "paper" or userInput.lower() == "scissors":
        break
    elif userInput.lower() == "quit":
        quit()
    else:
        print("Error: User did not input rock, paper, or scissors.")

computerChoiceOptions = ["Rock", "Paper", "Scissors"]
computerChoice = computerChoiceOptions[random.randint(0, 2)]

# Checks for ties
if computerChoice == userInput:
    print(f"The computer picked {computerChoice} and the user picked {userInput}\nThis means it is a tie, try again!")
# Checks for losses
elif computerChoice == "Paper" and userInput.capitalize() == "Rock":
    print(f"The computer picked {computerChoice} and the user picked {userInput}\nThis means that the computer beat you, try again!")
elif computerChoice == "Rock" and userInput.capitalize() == "Scissors":
    print(f"The computer picked {computerChoice} and the user picked {userInput}\nThis means that the computer beat you, try again!")
elif computerChoice == "Scissors" and userInput.capitalize() == "Paper":
    print(f"The computer picked {computerChoice} and the user picked {userInput}\nThis means that the computer beat you, try again!")
# If code reaches here, the player won
else:
    print(f"The computer picked {computerChoice} and the user picked {userInput}\nThis means that you won! Congratulations!!!")
