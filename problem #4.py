################################################
# Author: keidy lopez
# filename: problem #4.py
# description: plays dice game against a computer
################################################
import die
import time

def main():
    # welcome statement
    print('This program plays a dice game with the computer.')
    time.sleep(1.2)

    # condition and while loop to play the game
    my_coondition = True
    while my_coondition:
        dice = (die.Die().Roll(),die.Die().Roll())              # creates a tuple with die objects
        print('\nRolling the dice - get ready to place your bet!\n-.-.-.-.-.-.-.-.-.\n')
        time.sleep(2)
        print('Do you bet the roll is:\n')
        time.sleep(.5)
        choice = menuDisplay()              # displays menu options to player
        print()
        winner = isWinner(choice,sum(dice))  # determines winner
        if winner:
            time.sleep(.5)
            print('You Win! The sum of the roll was:', sum(dice))
        else:
            time.sleep(.5)
            print('you lost :(\nThe sum of the roll was:', sum(dice))
            time.sleep(.5)
        play = input('Do you want to play again (y/n): ')
        if play.upper() != 'Y':
            my_coondition = False


# displays menu options for player, makes sure the option is valid, and returns that choice
def menuDisplay():
    my_condition = True
    while my_condition:
        print('1. Over Seven')
        time.sleep(.5)
        print('2. Lucky Seven')
        time.sleep(.5)
        print('3. Under Seven')
        time.sleep(1)
        choice = int(input('\nPlease choose an option (1,2 or 3): '))
        if choice > 3 or choice <= 0:
            time.sleep(.2)
            print('please enter a valid choice number')
            time.sleep(.5)
        elif choice == 1 or choice == 2 or choice == 3:
            my_condition = False
            return choice

# decides if the player won or not based on the roll and choice
def isWinner(choice:int, rollsum:int)->bool:
    if choice==1 and rollsum > 7:
        return True
    elif choice==2 and rollsum ==7:
        return True
    elif choice == 3 and rollsum < 7:
        return True
    elif choice==1 and rollsum <= 7:
        return False
    elif choice==2 and rollsum !=7:
        return False
    elif choice == 3 and rollsum >= 7:
        return False


if __name__ == "__main__":
    main()