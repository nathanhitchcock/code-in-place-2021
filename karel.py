'''
First person Karel
Write a program that lets you play Karel in a rectangular world 
(moving and turning left and not walking off of the world, all that good stuff)!

Have you ever wanted to be Karel, wandering about a nice rectangular world, 
not a worry in the world, just moving and turning left whenever you'd like? 
You can emulate this feeling by writing a console-based first person Karel program! 
For simplicity, assume that beepers and painting are out of the question, 
and the world has no walls. All you should implement is moving and turning left. 
Store the number of columns and rows in your "world" as constants, and assume you 
start in row 1 column 1 facing East. Prompt the user for an action ("move" or 
"turn left" until they press enter without typing anything, in which case the result 
of input() will be an empty string, and you can stop looping).

Recall that you can only move if you're not about to move off of the world! 
This means you can only move in the following cases:

facing East and current column is less than the number of columns (move right)
facing West and current column is greater than 1 (move left)
facing North and current row is less than the number of rows (move up)
facing South and current row is greater than 1 (move down)

Here's what turning left does to the direction you (Karel) are facing:
if you're facing East, turning left will make you face North
if you're facing North, turning left will make you face West
if you're facing West, turning left will make you face South
if you're facing South, turning left will make you face East
'''


def main():
    # store the number of columns and rows in your "world" as constants
    # and assume you start in row 1 column 1 facing East
    ROW = 1
    COLUMN = 1
    DIRECTION = "East"
    MAX_COLUMNS = 10
    MAX_ROWS = 10

    # Prompt the user for an action "move" or "turn left"
    #  until they press enter without typing anything, 
    user_input = input("What would you like to do? You can move and turn left. Press enter to finish. ")

    while(user_input != None):
        if (user_input == "move"):
            COLUMN = move_column(COLUMN, MAX_COLUMNS, DIRECTION)
            ROW = move_row(ROW, MAX_ROWS, DIRECTION)
            # move_forward(ROW, MAX_ROWS, COLUMN, MAX_COLUMNS, DIRECTION)
            print("You moved one step forward and now you're at row " + str(ROW) + " column " +str(COLUMN))
        if (user_input == "turn left"):
            DIRECTION = turn_left(DIRECTION)

        user_input = input("What would you like to do? You can move and turn left. Press enter to finish. ")
        if (user_input == ""):
            print("thanks for all the fish!")
            break

def move_column(COLUMN, MAX_COLUMNS, DIRECTION):
    # we check for the end of the world first, so karel doesn't go outside of their plane of exisitence! 
    if (COLUMN == MAX_COLUMNS) and (DIRECTION == "East"):
        print("You've reached the end of the world! Try turning or something!")
    elif (COLUMN == 1) and (DIRECTION == "West"):
        print("You've reached the end of the world! Try turning or something!")
    # facing East and current column is less than the number of columns (move right)
    elif (DIRECTION == "East") and (COLUMN <= MAX_COLUMNS):
        COLUMN =  COLUMN + 1
    # facing West and current column is greater than 1 (move left)
    elif (DIRECTION == "West") and (COLUMN > 1):
        COLUMN =  COLUMN - 1
    return COLUMN

def move_row(ROW, MAX_ROWS, DIRECTION):
    if (ROW == MAX_ROWS) and (DIRECTION == "North"):
        print("You've reached the end of the world! Try turning or something!")
    elif (ROW == 1) and (DIRECTION == "South"):
        print("You've reached the end of the world! Try turning or something!")
    # facing North and current row is less than the number of rows (move up)
    if (DIRECTION == "North") and (ROW <= MAX_ROWS):
        ROW =  ROW + 1
    # facing South and current row is greater than 1 (move down)
    elif (DIRECTION == "South") and (ROW > 1):
        ROW =  ROW - 1
        
    # print("You moved one step forward and now you're at row " + str(ROW) + " column " +str(COLUMN))
    return ROW


def turn_left(DIRECTION):
    # if you're facing East, turning left will make you face North
    if (DIRECTION == "East"):
        DIRECTION = "North"
    # if you're facing North, turning left will make you face West
    elif (DIRECTION == "North"):
        DIRECTION = "West"
    # if you're facing West, turning left will make you face South
    elif (DIRECTION == "West"):
        DIRECTION = "South"
    # if you're facing South, turning left will make you face East
    elif (DIRECTION == "South"):
        DIRECTION = "East"
    # print and return the results
    print("You turned left and are now facing " + DIRECTION + ".")
    return DIRECTION
    




if __name__ == "__main__":
    main()
