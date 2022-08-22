import random
from time import sleep

board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-", ]

currentPlayer = "X"
winner = None
gameRunning = True

# printing the game board


def printBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("----------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("----------")
    print(board[6] + " | " + board[7] + " | " + board[8])

# take the player input


def playerInput(board):
    while True:
        try:
            inp = int(input("Enter a number 1-9: "))
            if 1 <= inp <= 9 and board[inp - 1] == "-":
                board[inp-1] = currentPlayer
                break
            elif inp not in range(1, 11):
                print("Enter a valid number!")
                printBoard(board)
            else:
                print("Try again, spot occupied!")
                printBoard(board)
        except ValueError:
            print("Enter a valid number!")
            printBoard(board)

# check for the win or tie(diagonally, horizontally or vertically)


def checkHorizontal(board):
    global winner
    if board[0] == board[1] == board[2] and board[1] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True


def checkVertical(board):
    '''Checks for matching values in column'''
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    if board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    if board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[2]
        return True


def checkDiagonal(board):
    '''Checks for matching values in diagonal of matrix'''
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    if board[2] == board[4] == board[7] and board[2] != "-":
        winner = board[2]
        return True


def checkTie(board):
    global gameRunning
    if "-" not in board:
        printBoard(board)
        print("It is a tie")
        exit(0)


def checkWin():
    global gameRunning
    if checkDiagonal(board) or checkHorizontal(board) or checkVertical(board):
        print(f"The winner is {winner}")
        gameRunning = False

# switch the player


def switchPlayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"


# computer
def computer(board):
    while currentPlayer == "O":
        position = random.randint(0, 8)
        if board[position] == "-":
            board[position] = "O"
            switchPlayer()
    sleep(0.3)


# check fo win or tie again
while gameRunning:
    printBoard(board)
    playerInput(board)
    checkWin()
    checkTie(board)
    switchPlayer()
    computer(board)
    checkWin()
    checkTie(board)

# TODO
# What happens when both people win?
# When a winner is announced check tie shouldnt run
# choose whether you want to play with computer or not
