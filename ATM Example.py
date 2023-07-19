#ATM EXAMPLE

card_no='05101520'
pin_no='2008'

user_card=input('Enter your card number: ')
user_pin=input('Enter your pin number: ')

def ATM():
    while True:
        balance=5000
        option=input('Select an option\n 1. Balance Enquiry\n 2. Withdraw\n 3. Deposit\n 4. Exit\n Enter the number here: ')
        if option=='1':
            print('Your current balance is: $',balance)
        elif option=='2':
            withdraw=int(input('Enter the amount you want to withdraw: $'))
            if balance<withdraw:
                print('Insuff. Money')
            else:
                balance=balance-withdraw
                print('Your current balance: $',balance)
        elif option=='3':
            deposit=int(input('Enter the amount you want to deposit: $'))
            balance=balance+deposit
            print('Your current balance is: $',balance)
        elif option=='4':
            break
        else:
            print('Select one of the options above')
            

if card_no==user_card and pin_no==user_pin:
    ATM()
else:
    print('Invalid User')

  
