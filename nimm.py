"""
Nimm game description:
--------------------------------
The game starts with a pile of 20 stones between the players.
The two players alternate turns.
On a given turn, a player may take either 1 or 2 stone from the center pile.
The two players continue until the center pile has run out of stones.
"""

def main():
    # variable declaration
    total_stones = 20
    p1_stones = 0
    p2_stones = 0
    max_players = 2
    #TODO - create a player number array to specify dynamic number of players for the game
    #TODO - create a check for the user input to validate only correct numbers are given as input

    stone_report(total_stones)

    # each player takes a turn, may take 1 or 2 stones (user_input)
    while (total_stones >= 1):

        # we initate the player_number and increment it as the loop progresses
        player_number = 0
        '''
        3 items happen per turn:
        - check_endgame to see if the game is over before the player's turn starts
        - update the player number
        - take_turn goes through the stone selection and displays the updated count to screen
        '''

        for i in range (max_players):
            check_endgame(total_stones, player_number)
            player_number = player_number + 1
            total_stones = take_turn(player_number, total_stones)
            stone_report(total_stones)
        check_endgame(total_stones, player_number)

# check to see if there is an endgame
def check_endgame(total_stones, player_number):
    if (total_stones <= 0):
        #print("Game Over!")
        if (int(player_number) == 1):
            print("Player 2 wins!")
        else:
            print("Player 1 wins!")
        exit()
    else:
        pass

# display the number of stones left
def stone_report(total_stones):
    print("\n" + "There are " + str(total_stones) + " stones left")

# take_turn goes through the stone selection and displays the updated count to screen
def take_turn(player_number, total_stones):
    answer = input("Player " + str(player_number) + " would you like to remove 1 or 2 stones? ")
    if (int(answer) == int(1) or int(2)):
        total_stones = total_stones - int(answer)
    return(total_stones)

if __name__ == '__main__':
    main()
