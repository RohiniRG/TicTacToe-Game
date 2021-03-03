import utility


def multi_player():
    player1, player2, turn = utility.player_assignment(2)
    name = player1
    board = utility.reset_board()
    utility.print_board(board)

    count = 0

    for i in range(10):
        # Taking input from the user b/w 0 to 9
        exist = 1
        while exist:
            print(f"{name}'s chance!!!. Choose an occupied space :")

            try:
                user_input = int(input())
            except ValueError:
                print("Invalid Input")
                print("!!!Enter Again!!!")
                exist = 1
                continue

            if 0 < user_input < 10:
                # IF true then checking if the space is already occupied
                if board[user_input] == " ":
                    board[user_input] = turn
                    count += 1
                    exist = 0
                else:
                    print("Space already occupied")
                    exist = 1

            else:
                print("Invalid Input")
                print("!!!Enter Again!!!")
                exist = 1

        utility.print_board(board)

        # min count required is 5 to check if one wins or not
        if count >= 5:

            # Horizontal Lines
            if board[7] == board[8] == board[9] != " ":
                if board[7] == turn:
                    print(f"{player1} WINS")
                else:
                    print(f'{player2} WINS')
                break

            elif board[4] == board[5] == board[6] != " ":
                if board[4] == turn:
                    print(f"{player1} WINS")
                else:
                    print(f'{player2} WINS')
                break

            elif board[1] == board[2] == board[3] != " ":
                if board[1] == turn:
                    print(f"{player1} WINS")
                else:
                    print(f'{player2} WINS')
                break

            # Vertical Line
            elif board[7] == board[4] == board[1] != " ":
                if board[7] == turn:
                    print(f"{player1} WINS")
                else:
                    print(f'{player2} WINS')
                break

            elif board[8] == board[5] == board[2] != " ":
                if board[8] == turn:
                    print(f"{player1} WINS")
                else:
                    print(f'{player2} WINS')
                break

            elif board[9] == board[6] == board[3] != " ":
                if board[9] == turn:
                    print(f"{player1} WINS")
                else:
                    print(f'{player2} WINS')
                break

            # Diagonals
            elif board[7] == board[5] == board[3] != " ":
                if board[7] == turn:
                    print(f"{player1} WINS")
                else:
                    print(f'{player2} WINS')
                break

            elif board[9] == board[5] == board[1] != " ":
                if board[9] == turn:
                    print(f"{player1} WINS")
                else:
                    print(f'{player2} WINS')
                break

        # if no one wins
        if count == 9:
            print("Match Tie")
            break

        # To interchange players
        if turn == "X":
            turn = "0"
        else:
            turn = "X"

        if name == player1:
            name = player2
        else:
            name = player1
