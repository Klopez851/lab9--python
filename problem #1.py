################################################
# Author: keidy lopez
# filename: problem #1.py
# description: driver program that instantiates the Die class and rolls a pair of dice 5 times.
################################################
import die

def main():
    # welcome statement
    print('Welcome to the dice rolls!')

    # creates a Die object
    roll = die.Die()

    # for loop that prints out 5 dice rolls using the Die object
    for i in range(5):
        print('Roll',i+1,':',roll.Roll(),roll.Roll())

    print('Done!')

if __name__=="__main__":
    main()