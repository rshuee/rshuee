#GUESS THE NUMBER

from random import*
s=randrange(1,100)

print('You need to guess the number between 1 to 100\n You have 5 chances\n Try your luck!')

for i in range(5):
    user_num=int(input('Enter the number you have guessed: '))
    if user_num>s:
        print('The number is too high')
    elif user_num<s:
        print('The number is too low')
    else:
        print('Hurray, you have chosen my number!')
        break
print('The number was:',s)


