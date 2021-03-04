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

def interchange_players_turns(player1, player2,name, turn):
    if turn == "X":
        turn = "0"
    else:
        turn = "X"

    if name == player1:
        name = player2
    else:
        name = player1

    return turn,name

def checking_count(count, board):
    if count >= 5:

        # Horizontal Lines
        if board[7] == board[8] == board[9] != " ":
            return board[7]

        elif board[4] == board[5] == board[6] != " ":
            return board[4]

        elif board[1] == board[2] == board[3] != " ":
            return board[1]

        # Vertical Line
        elif board[7] == board[4] == board[1] != " ":
            return board[7]

        elif board[8] == board[5] == board[2] != " ":
            return board[8]

        elif board[9] == board[6] == board[3] != " ":
            return board[9]

        # Diagonals
        elif board[7] == board[5] == board[3] != " ":
            return board[7]

        elif board[9] == board[5] == board[1] != " ":
            return board[9]

    # if no one wins
    if count == 9:
        return "red"
