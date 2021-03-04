import random
playerName_move = {}

def player_assignment(num):
    player1 = input("Enter the Name of PLAYER 1: ")
    player2 = 'Computer'
    if num == 2:
        player2 = input("Enter the Name of PLAYER 2: ")

    while True:
        turn = input(f"{player1} choose X or 0: ").upper()
        
        if turn == "X":
            turn2 = "0"
            playerName_move[turn2] = player2
        else:
            turn2 = "X"
            playerName_move[turn2] = player2

        playerName_move[turn] = player1

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
    

def comp_chance(possibleMoves, board, count):
    
    for chance in ["X", "0"]:
        for i in possibleMoves:
            boardCopy = board.copy()
            boardCopy[i] = chance
            comp_move = checking_count(count, boardCopy)
            if comp_move:
                return i
        
    cornersOpen = []
    for i in possibleMoves:
        if i in [1,3,9,7]:
            cornersOpen.append(i)

    if len(cornersOpen) > 0:
        comp_move = random.choice(cornersOpen)
        return comp_move

    if 5 in possibleMoves:
        comp_move = 5
        return comp_move

    edgesOpen = []
    for i in possibleMoves:
        if i in [8,4,2,6]:
            edgesOpen.append(i)

    if len(edgesOpen) > 0:
        comp_move = random.choice(edgesOpen)
        return comp_move

    

