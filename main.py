import SinglePlayer
import MultiPlayer

print('\n----****!!Welcome to TicTacToe game!!****----')

loop = 1
while 1:
    print("\n\tMENU:")
    print('\t\t1. Single Player\n\t\t2. Multi Player\n\t\t3. Exit Game')
    try:
        choice = int(input('\nSelect your choice: '))
        if choice == 1:
            SinglePlayer.single_player()
            pass
        elif choice == 2:
            MultiPlayer.multi_player()
            pass
        elif choice == 3:
            print('It was fun having you!!\n\nExiting game....\n\n')
            # loop = 0
            break
        else:
            print('Invalid Entry!')
    except ValueError:
        print('Invalid Entry!')

    print('\nGoing back to the MENU....')
