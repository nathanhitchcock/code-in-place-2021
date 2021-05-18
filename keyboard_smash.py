import random
from TextGrid import TextGrid

SMASHABLE_LETTERS = ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ';']
NUM_LETTERS = 10

def main():
    grid = TextGrid.blank(NUM_LETTERS, 1)
    
    # use a foreach loop to iterate through the cells in the grid
    for cell in grid:
        # generate a random calue and place it in the grid
        cell.value = get_random_value()

    
    print(grid)

def get_random_value():
    idx = random.randint(0,len(SMASHABLE_LETTERS) - 1) # randomly generate an index
    return SMASHABLE_LETTERS[idx] # return alphabetic letter

if __name__ == '__main__':
    main()
