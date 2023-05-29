"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Rostislav Vymazal
email: rostislav.vymazal@centrum.cz
discord: Rostislav V.
"""


def print_board(board):
    print("+---+---+---+")
    for row in board:
        print("| {} | {} | {} |".format(*row))
        print("+---+---+---+")


def make_move(board, player):
    while True:
        move = input(f"Player {player} | Please enter your move number: ")
        if not move.isdigit():
            print("Invalid input. Please enter a number.")
            continue
        move = int(move) - 1
        if not 0 <= move <= 8:
            print("Invalid move. Please enter a number between 1 and 9.")
            continue
        row = move // 3
        col = move % 3
        if board[row][col] != " ":
            print("Invalid move. This position is already occupied.")
            continue
        board[row][col] = player
        break


def has_winner(board):
    # check rows
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != " ":
            return row[0]
    # check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]
    # check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]
    # no winner
    return None


def play_game():
    print("Welcome to Tic Tac Toe")
    print("========================================")
    print("GAME RULES:")
    print("Each player can place one mark (or stone)")
    print("per turn on the 3x3 grid. The WINNER is")
    print("who succeeds in placing three of their")
    print("marks in a:")
    print("* horizontal,")
    print("* vertical or")
    print("* diagonal row")
    print("========================================")
    print("Let's start the game")

    board = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "],
    ]

    player = "x"

    while True:
        print("----------------------------------------")
        print_board(board)
        make_move(board, player)
        winner = has_winner(board)
        if winner:
            print("----------------------------------------")
            print_board(board)
            print(f"Congratulations, the player {winner} WON!")
            break
        elif all(cell != " " for row in board for cell in row):
            print("----------------------------------------")
            print_board(board)
            print("It's a tie!")
            break
        player = "o" if player == "x" else "x"


play_game()

