"""
Number Guesser Program

This is an example of how to use variables to 
keep track of information in a program that 
also makes use of loops
"""
import numpy as np


def guess_a_number(MIN_NUM, MAX_NUM):
    if MIN_NUM == MAX_NUM:
        guess = MIN_NUM
    else:
        guess = int(np.random.randint(MIN_NUM, MAX_NUM, size=(1,)))
    return guess

def get_user_input(guess):
    u_input = input("Is your number " + str(guess) + "? ")
    return u_input

def main():
    MIN_NUM = 0
    MAX_NUM = 100
    # generate an inital guess
    guess = guess_a_number(MIN_NUM, MAX_NUM)
    # convert the guess to an int to remove the []
    guess = int(guess)
    # collect the inital user input
    u_input = get_user_input(guess)
    # initiatize the count
    count = 1

    #TODO - implement the 'by half' strategy for guessing subsequent numbers
    while u_input != "correct":
        count = count + 1

        # lower, meaning that the correct number is less than what the computer guessed
        # we will set the MAX_NUM value to the guess and re-try
        if u_input == "lower":
            MAX_NUM = guess - 1
            print("the MAX_NUM is",MAX_NUM)
            guess = guess_a_number(MIN_NUM, MAX_NUM)
            u_input = get_user_input(guess)

        # higher, meaning that the correct number is greater than what the computer guessed
        # we will set the MIN_NUM value to the guess and re-try
        if u_input == "higher":
            MIN_NUM = guess + 1
            print("the MIN_NUM is",MIN_NUM)
            guess = guess_a_number(MIN_NUM, MAX_NUM)
            u_input = get_user_input(guess)

    #print out the results
    print("I win! It took me " + str(count) + " guesses")

    

if __name__ == "__main__":
    main()
