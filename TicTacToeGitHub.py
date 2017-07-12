import random

board = [i for i in range(10)]


def print_board():
    print("   |   |   ")
    print(" " + str(board[1]) + " | " + str(board[2]) + " | " + str(board[3]) + " ")
    print("   |   |   ")
    print("---|---|---")
    print("   |   |   ")
    print(" " + str(board[4]) + " | " + str(board[5]) + " | " + str(board[6]) + " ")
    print("   |   |   ")
    print("---|---|---")
    print("   |   |   ")
    print(" " + str(board[7]) + " | " + str(board[8]) + " | " + str(board[9]) + " ")
    print("   |   |   ")


def check_for_win(XorO):
    if      (board[1] == XorO and board[2] == XorO and board[3] == XorO) or \
            (board[4] == XorO and board[5] == XorO and board[6] == XorO) or \
            (board[7] == XorO and board[8] == XorO and board[9] == XorO) or \
            (board[1] == XorO and board[4] == XorO and board[7] == XorO) or \
            (board[2] == XorO and board[5] == XorO and board[8] == XorO) or \
            (board[3] == XorO and board[6] == XorO and board[9] == XorO) or \
            (board[1] == XorO and board[5] == XorO and board[9] == XorO) or \
            (board[3] == XorO and board[5] == XorO and board[7] == XorO):
        print('\n\n\n\n\n\n\n' + XorO + ' has won the game!')
        print_board()
        return False
    else:
        return True


def validateInputPlayerLetter():
    while True:
        input_X_or_O = input().upper()
        if input_X_or_O == 'X' or input_X_or_O == 'O':
            return input_X_or_O
        else:
            # os.system("clear")
            print('Not an X or an O. Try again...\n')


def whoGoesFirst():
    if random.randint(0, 1) == 1:
        print('The Human will go first')
        return 'Human'
    else:
        print('The MegaBot will go first')
        return 'MegaBot'


def inputPlayerLetter():
    # Lets the player type which letter they want to be.
    # Returns a list with the player’s letter as the first item, and the computer's letter as the second.
    print('Do you want to be X or O?')
    letter = validateInputPlayerLetter()  # input().upper()
    # the first element in the list is the player’s letter, the second is the computer's letter.
    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']


def validateHumanSelection():
    human_selection = input('Please select an available space 1-9:\n')
    while True:
        try:
            human_selection = int(human_selection)
            if 0 < human_selection < 10:
                if board[human_selection] != 'X' or board[human_selection] != 'Y':
                    return human_selection
                else:
                    print('That space is already taken by ' + str(board[human_selection]))
            else:
                print('You need to choose a number that is 1-9 not ' + str(human_selection))

        except ValueError:
            print('Please choose an integer that is 1-9')


def getComputerSelection():
    # must return the array to be chosen
    return 1


# Build computers AI
# Add doc strings to each function
# Add unit tests
# Enhance the abstraction

def gameRunner():
    player_letter, computer_letter = inputPlayerLetter()
    player_state = whoGoesFirst()
    game_state = True
    while game_state:
        if player_state == 'Human':
            print_board()
            board_array_location = validateHumanSelection()
            board[board_array_location] = player_letter
            game_state = check_for_win(player_letter)
            player_state = 'MegaBot'
        elif player_state == 'MegaBot':
            board_array_location = getComputerSelection()
            board[board_array_location] = computer_letter
            game_state = check_for_win(computer_letter)
            player_state = 'Human'
        else:
            print("You're a shitty programmer if you see this code in the console")
            #chose not to write break
            game_state = False


if __name__ == '__main__':
    """Runs the one time events tied to setup
       of the game. Then it will fire the looped
       events where the game truly runs"""
    print('Welcome to Tic Tac Toe')
    gameRunner()