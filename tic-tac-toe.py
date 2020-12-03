def main():
    # Creates the board, numpad styled values
    board = {
        '7': ' ' , '8': ' ' , '9': ' ' ,
        '4': ' ' , '5': ' ' , '6': ' ' ,
        '1': ' ' , '2': ' ' , '3': ' ' ,
    }

    # To stop input that is not 1 - 9.
    inputChecker = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

    # The board the player sees.
    def displayBoard():
        print(f"{board['7']}|{board['8']}|{board['9']}")
        print("-+-+-")
        print(f"{board['4']}|{board['5']}|{board['6']}")
        print("-+-+-")
        print(f"{board['1']}|{board['2']}|{board['3']}")
        return

    # To check if player wants to restart game
    def restart():
        choice = input("Do you want to play again?[yes/no] -- ")
        yes = ["yes", "y"]
        if choice.lower() in yes:
            main()
        else:
            print("Have a good day!")
            quit()

    # Checks for ties
    def tie():
        forCheck = 0
        for val in board:
            if board[val] != " ": forCheck += 1
        if forCheck == 9: return True
        return False

    ### MINI CHECKERS ###
    # If return true, then game over
    def rowChecker():
        if board['7'] == board['8'] == board['9'] and board['7'] != " ": return True
        if board['4'] == board['5'] == board['6'] and board['4'] != " ": return True
        if board['1'] == board['2'] == board['3'] and board['1'] != " ": return True
        return False

    def columnChecker():
        if board['7'] == board['4'] == board['1'] and board['7'] != " ": return True
        if board['8'] == board['5'] == board['2'] and board['8'] != " ": return True
        if board['9'] == board['6'] == board['3'] and board['9'] != " ": return True
        return False

    def diagonalChecker():
        if board['7'] == board['5'] == board['3'] and board['7'] != " ": return True
        if board['9'] == board['5'] == board['1'] and board['9'] != " ": return True
        return False

    ### MAIN CHECKER ###
    # With logical or, if any checks come back true, the result is true.
    def checker():
        return rowChecker() or columnChecker() or diagonalChecker()

    ### MAIN CODE ##################################################################
    def game():
        turn = 'X'
        counter = 0

        while True:
            displayBoard()
            print(f"\nIt is {turn}'s turn, where do you wanna place your piece?")
            print("P.S. It goes according to a numpad.")

            move = input()
            if move in inputChecker:
                pass
            else:
                print("\nError: Invalid Input\n")
                continue

            if board[move] == " ":
                board[move] = turn
                counter += 1
            else:
                print("\nError: That spot is taken, which spot do you want?\n")
                continue

            # Swaps turns
            if turn == "X":
                turn = "O"
            else:
                turn = "X"
        
            # Checks for logical finishes
            if counter >= 5:
                if tie():
                    displayBoard()
                    print("\nGame Over! It's a tie!")
                    restart()
                if checker():
                    displayBoard()
                    print("\nGame Over!")
                    restart()

    ## Runs the game ##
    game()
main()