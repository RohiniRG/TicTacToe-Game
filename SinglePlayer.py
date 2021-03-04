import utility
import random


def single_player():
    player1, _, turn = utility.player_assignment(1)
    comp = 'Computer'
    name = player1
    unoccupied = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    board = utility.reset_board()
    utility.print_board(board)

    count = 0

    for i in range(10):
        # Taking input from the user b/w 0 to 9
        exist = 1
        while exist:
            print(f"{name}'s chance!!!. Choose an unoccupied space :")

            if name == player1:
                try:
                    user_input = int(input())
                except ValueError:
                    print("Invalid Input")
                    print("!!!Enter Again!!!")
                    exist = 1
                    continue

            else:
                user_input = utility.comp_chance(unoccupied, board, count)

            

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

        unoccupied.remove(user_input)

        utility.print_board(board)

        if count == 9:
            print("Match Tie")
            break

        ans = utility.checking_count(count, board)

        if ans == 'X' or ans == '0':
            name = utility.playerName_move[ans]
            print(f"{name} WINS")
            break

        # To interchange players        
        turn, name = utility.interchange_players_turns(player1,comp,name,turn)
