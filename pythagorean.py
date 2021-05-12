import math

def main():
    '''
    Your code should read in the lengths of the sides 
    AB and AC, and that outputs the length of the 
    hypotenuse (BC). You will probably find math.sqrt() 
    to be useful.
    '''
    # collect user input
    AB = input("Enter the length of AB: ")
    AC = input("Enter the length of AC: ")

    # convert the input to floats 
    # (error when combined in the same line above)
    AB = float(AB)
    AC = float(AC)

    # perform calculation
    BC = perform_pythangorean(AB,AC)

    # print result
    print("The length of BC (the hypotenuse) is: " + str(BC))


def perform_pythangorean(AB,AC):
    return math.sqrt(AB) + math.sqrt(AB)

if __name__ == "__main__":
    main()
