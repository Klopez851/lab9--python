################################################
# Author: keidy lopez
# filename: problem #2.py
# description:program that uses the Die class to roll a dice until doubles are rolled
################################################
import die
def main():
    # welcome statement
    print('Welcome to the doubles trials!')

    # condition for while loop
    my_condition = True

    # accumulator variable
    counter = 0

    # while loop that prints out and counts dice rolls until doubles are rolled
    while my_condition:
        roll1 = die.Die().Roll()
        roll2 = die.Die().Roll()
        if roll1 == roll2:
            print('Roll:', roll1, roll2, ' <- Doubles!')
            counter+=1
            my_condition = False
        else:
            print('Roll:', roll1, roll2)
            counter+=1

    # tells user the amount in accumulator variabl
    print('It took', counter,'roll(s) to roll doubles!')




if __name__ == "__main__":
    main()