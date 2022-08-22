#!/usr/bin/python3
'''Dictionary implementation of board'''

board = {1: ' ', 2: ' ', 3: ' ',
         4: ' ', 5: ' ', 6: ' ',
         7: ' ', 8: ' ', 9: ' '}
player = 'O'
computer = 'X'


def printBoard(board):
    print(" " + board[1] + " | " + board[2] + " | " + board[3])
    print("---+---+---")
    print(" " + board[4] + " | " + board[5] + " | " + board[6])
    print("---+---+---")
    print(" " + board[7] + " | " + board[8] + " | " + board[9])
    print("\n")


def spaceisFree(position):
    if board[position] == ' ':
        return True
    return False


def insertLetter(letter, position):
    if spaceisFree(position):
        board[position] = letter
        printBoard(board)
        if checkDraw():
            print("Draw")
            exit()
        if checkWin():
            if letter == 'X':
                print("Bot wins!")
                exit()
            else:
                print("Player wins!")
                exit()
        return
    else:
        print("Invalid position!")
        while True:
            try:
                position = int(input("Please enter a new position: "))
                if 1 <= position <= 9:
                    insertLetter(player, position)
                    break
                elif position not in range(1, 11) or position == '':
                    print("Enter a valid number!")
                else:
                    print("Enter a number bewteen 1 and 9")
            except ValueError:
                print("Enter a number!")


def checkWin():
    # check horizontal
    if (board[1] == board[2] and board[1] == board[3] and board[1] != ' '):
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] != ' '):
        return True
    elif (board[7] == board[8] and board[7] == board[9] and board[7] != ' '):
        return True
    # check vertical
    elif (board[1] == board[4] and board[1] == board[7] and board[1] != ' '):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] != ' '):
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] != ' '):
        return True
    # check diagonal
    elif (board[1] == board[5] and board[1] == board[9] and board[1] != ' '):
        return True
    elif (board[7] == board[5] and board[7] == board[3] and board[7] != ' '):
        return True
    else:
        return False


def checkDraw():
    for key in board.keys():
        if board[key] == ' ':
            return False
    return False


def playerMove():
    while True:
        try:
            position = int(input("Enter position for 'O': "))
            if 1 <= position <= 9:
                insertLetter(player, position)
                break
            elif position not in range(1, 11) or position == '':
                print("Enter a valid number!")
            else:
                print("Enter a number bewteen 1 and 9")
        except ValueError:
            print("Enter a number!")

    return


def computerMove():
    while True:
        try:
            position = int(input("Enter position for 'X': "))
            if 1 <= position <= 9:
                insertLetter(computer, position)
                break
            elif position not in range(1, 11) or position == '':
                print("Enter a valid number!")
            else:
                print("Enter a number bewteen 1 and 9")
        except ValueError:
            print("Enter a number!")
    return


while not checkWin():
    computerMove()
    playerMove()

printBoard(board)
