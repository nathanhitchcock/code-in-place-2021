import random

'''
Write a program which will flip a weighted coin.

Coin flips are usually fair, but can be cheated -- a weighted coin
 is a coin where the probability of heads isn't 50%. 
Your code should use the random module to "flip" coin where the 
probability of heads is 70% and print the outcome (heads or tails).
'''
    
def main():
    #ask the user how many flips would they like to make
    N = input("How many flips? ")
    N = int(N)

    #perform the flips
    result = flip_coin(N)

# we set the probability of flipping heads to 70%
def flip_coin(N, prob_true=0.7):
    # establish the local counters
    heads = 0
    tails = 0

    # using the user's input we run through the flips, adding up the number of heads and tails
    for i in range(N):
        flip = random.random() < prob_true
        if flip == True:
            heads += 1
        else:
            tails += 1
            
    # we print the results at the end
    print ("heads were flipped " + str(heads) + " times")
    print ("tails were flipped " + str(tails) + " times")



if __name__ == "__main__":
    main()
