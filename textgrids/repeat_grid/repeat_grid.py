from TextGrid import TextGrid

DEFAULT_FILENAME = 'abcd.txt'
NUM_REPEATS = 2

def main():
    grid = TextGrid(DEFAULT_FILENAME)
    print("Initial grid:")
    print(grid)
    final_grid = TextGrid.blank(NUM_REPEATS * grid.width, grid.height)
    
    # TODO: your code here!
    

    print("Final grid:")
    print(final_grid)


if __name__ == '__main__':
    main()
