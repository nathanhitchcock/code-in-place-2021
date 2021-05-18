from TextGrid import TextGrid
import random

DEFAULT_FILENAME = 'zero_one.txt'

def main():
    grid = TextGrid(DEFAULT_FILENAME)
    print("Initial grid:")
    print(grid)

    #TODO - I've gotten the grid to repeat, but why isn't it performing the replacement?
    for cell in grid:
        value = cell.value
        cell.value = get_cell_value(value, grid)
    print("New grid:")
    print(grid)

def get_cell_value(value, grid):
    if value == '0':
        value == '1'
    if value == '1':
        value == '0'
    return value


if __name__ == '__main__':
    main()
