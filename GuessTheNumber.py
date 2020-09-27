import random

# Sets the computer's number
number = random.randint(1,20)

# Error checks to make sure user puts in number between 1 - 20
while True:
    userInput = input("Try to guess the number!\nEnter a number 1 - 20: ")
    try: 
        float(userInput)
    except:
        print("Error: That is not a number!")
        continue
    userInput = float(userInput)
    userInput = round(userInput)
    if userInput >= 1 and userInput <= 20:
        break
    else:
        print("Error: That number is not between 1 and 20!")
        continue

# One check before the next loop
if userInput == number:
    print("Congradulations! You guessed the number.")
    quit()
if userInput < number:
    print("Hint: Higher")
else: 
    print("Hint: Lower")

# Loops till the user is correct
while True:
    userInput = input("Enter a number 1 - 20: ")
    try: 
        float(userInput)
    except:
        print("Error: That is not a number!")
        continue
    userInput = float(userInput)
    userInput = round(userInput)
    if userInput >= 1 and userInput <= 20:
        pass
    else:
        print("Error: That number is not between 1 and 20!")
        continue
    if userInput == number:
        print("Congradulations! You guessed the number.")
        break
    if userInput < number:
        print("Hint: Higher")
        continue
    else:
        print("Hint: Lower")
