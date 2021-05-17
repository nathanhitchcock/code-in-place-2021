"""
Implements the game of Rock-Paper-Scissors!

History:
This classic game dates back to the Han Dinesty, over 2200 years ago.
The First International Rock-Paper-Scissors Programming Competition 
was held in 1999 and was won by a team called "Iocaine Powder"

The Game:
Each player choses a move (simultaneously) from the choices:
rock, paper or scissors. 
If they chose the same move the game is a tie. Otherwise:
rock beats scissors
scissors beats paper
paper beats rock.

In this program a human plays against an AI. The AI choses randomly
(we promise). The game is repeated N_GAMES times and the human gets
a total score. Each win is worth +1 points, each loss is worth -1
"""
import random

N_GAMES = 3

def main():
    #print welcome and initaize the variables 
    #(chicken & egg problem on first turn with human_move and logic in ai_move)
    print_welcome()
    total_score = 0
    winner = None
    human_move = None
    ai_move = None
    # 1. get the moves
    for i in range (N_GAMES):
        ai_move = get_ai_move(i, winner, human_move, ai_move)
        human_move = get_human_move()
        winner = get_winner(ai_move, human_move)
        total_score = update_score(winner, total_score)
        print('ai move was ', ai_move)
        print('human move was ', ai_move)
        print('winner was ', winner)
        print('')
    print('total score', total_score)

def update_score(winner, total_score):
    if winner == 'ai':
        total_score -= 1
    if winner == 'human':
        total_score += 1
    if winner == 'tie':
        total_score += 0
    return total_score

def get_ai_move(i, winner, human_move, ai_move):
    """
    the optimal strategy is:
    if you lose, switch to the thing that beats the thing your opponent just played. 
    if you win, switch to the thing that would beat the thing that you just played.
    """
    #if it's the first round, choose randomly 
    if (i == 0) or (winner == 'tie'):
        choices = ['rock', 'paper', 'scissors']
        ai_move = random.choice(choices)
        return ai_move
    #if it's the 2nd or 3rd round, review the winner & last human_move before deciding
    else:
        if winner == 'human':
            if human_move == 'rock':
                return 'paper'
            if human_move == 'paper':
                return 'scissors'
            if human_move == 'scissors':
                return 'rock'
        if winner == 'ai':
            if ai_move == 'rock':
                return 'paper'
            if ai_move == 'paper':
                return 'scissors'
            if ai_move == 'scissors':
                return 'rock'


def get_human_move():
    """
    returns a valid move from the human (rock, paper, or scissors)
    """
    while True:
        human_move = input('enter your move: ')
        if is_valid_move(human_move):
            return human_move
        print('invalid move')

def is_valid_move(move):
    """
    parameter move: string represeting what the user entered
    return: boolean which is True if the move was valid
    >>> is_valid_move('rock')
    True
    >>> is_valid_move('unicorn')
    False
    """
    if move == 'rock':
        return True
    if move == 'paper':
        return True   
    if move == 'scissors':
        return True
    return False


def get_winner(ai_move, human_move):
    """
    return: 'ai', 'human', or 'tie'
    depedning on who won 
    >>> get_winner('rock', 'scissors')
    'ai'
    >>> get_winner('scissors', 'rock')
    'human'
    >>> get_winner('rock', 'rock')
    'tie'
    """
    if ai_move == human_move:
        return 'tie'
    if ai_move == 'rock':
        if human_move == 'scissors':
            return 'ai'
        return 'human'
    if ai_move == 'paper':
        if human_move == 'rock':
            return 'ai'
        return 'human'
    if ai_move == 'scissors':
        if human_move == 'paper':
            return 'ai'
        return 'human'
    print('you should not get here.... ')

def print_welcome():
    print('Welcome to Rock Paper Scissors')
    print('You will play '+str(N_GAMES)+' games against the AI')
    print('rock beats scissors')
    print('scissors beats paper')
    print('paper beats rock')
    print('----------------------------------------------')
    print('')

if __name__ == '__main__':
    main()
