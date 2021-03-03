def player_assignment(num):
    player1 = input("Enter the Name of PLAYER 1: ")
    player2 = None
    if num == 2:
        player2 = input("Enter the Name of PLAYER 2: ")

    while True:
        turn = input(f"{player1} choose X or 0: ").upper()

        if turn == "X" or turn == "0":
            # player1_turn = turn
            return player1, player2, turn
        else:
            print('Invalid Entry! **You can only choose between X or 0!!**')


def print_board(board):
    print()
    print("\t\t" + " " + board[7] + " | " + board[8] + " | " + board[9])
    print("\t\t" + "---+---+---")
    print("\t\t" + " " + board[4] + " | " + board[5] + " | " + board[6])
    print("\t\t" + "---+---+---")
    print("\t\t" + " " + board[1] + " | " + board[2] + " | " + board[3])


def reset_board():
    board = {7: ' ', 8: ' ', 9: ' ',
             4: ' ', 5: ' ', 6: ' ',
             1: ' ', 2: ' ', 3: ' '}

    return board
