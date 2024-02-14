################################################
# Author: keidy lopez
# filename: problem #3.py
# description: driver test program for account class
################################################
from account import Account
import time

def main():
    # variables to set up account object
    account_number = int(input('What is your account number: '))
    opening_amount = float(input('What is the opening amount(cents included): '))

   # stylizing elements
    print()
    print('Creating account...\n')
    time.sleep(1)

    # account object
    personal_account = Account(account_number, opening_amount)

 # confirms entered info to the user
    print('account #:', personal_account.getAccountNumber())
    print('\tyour current balance is:', personal_account.getBalance())
    time.sleep(.5)

    # while loop for all the methods of the account object
    my_condition = True
    while my_condition:
        print('What would you like to do?')
        answer = Display()
        # tests deposit method
        if answer == 1:
            amount = float(input('How much would you like to deposit(cents included)? '))
            personal_account.deposit(amount)
            time.sleep(.7)
            print('\ncompleting transaction...\n')
            time.sleep(1)
            print('Done!\n')
        # tests withdraw method
        elif answer == 2:
            amount = float(input('How much would you like to withdraw(cents included)? '))
            personal_account.withdraw(amount)
            time.sleep(1)
            print('Done!\n')
        # tests balance method
        elif answer == 3:
            print('\nyour account balance is:', personal_account.getBalance(),'\n')
        # tests account method
        elif answer == 4:
            print('\nyour account number is:', personal_account.getAccountNumber(),'\n')
        # breaks out of while loop
        elif answer == 5:
            my_condition = False


# displays options and validates input
def Display():
    print('1.Deposit\n2.Withdraw\n3.See balance\n4.Account Number\n5.Quit')
    answer = int(input('enter choice here: '))
    if answer > 5 or answer <=0:
        print('\nplease enter a valid choice!\n')
    else:
        return answer


if __name__ == "__main__":
    main()