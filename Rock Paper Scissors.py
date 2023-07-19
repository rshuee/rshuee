#ROCK PAPER SCISSORS 

import random

x=0
while x<4:
    player_1=int(input('1. Rock\n2. Paper\n3. Scissors\n\nSelect an option: '))
    player_2=random.randrange(1,4)

    print('\nThe computer had chosen',player_2)

    if player_1==player_2:  
        print('A draw!')
        
    elif player_1==1:
        if player_2==2:
            print('The computer has won!')
        else:
            print('You won!')

    elif player_1==2:
        if player_2==1:
            print('You won!')
        else:
            print('he computer has won!')

    elif player_1==3:
        if player_2==1:
            print('The computer has won!')
        else:
            print('You won!')

    else:
        print('Invalid Option')
    x=x+1
