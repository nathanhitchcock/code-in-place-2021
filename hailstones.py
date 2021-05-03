"""
Hailstones
A separate (optional) problem you could consider writing is based on a problem
in Douglas Hofstadter’s Pulitzer-prize-winning book Gödel, Escher, Bach.
That book contains many interesting mathematical puzzles,
many of which can be expressed in the form of computer programs.

In Chapter XII, Hofstadter mentions a wonderful problem that is well within the scope of what you know.
The problem can be expressed as follows:

Pick some positive integer and call it n.
If n is even, divide it by two.
If n is odd, multiply it by three and add one.
Continue this process until n is equal to one.
"""
#initate the counter
counter = 0
# input number from user
input = int(input("Enter a number: "))

def main(input,counter):

    while (input != 1):
        #determine if that number is odd or even
        if (input % 2) == 0:
            #perform math << allow for floats
            response = float(input / 2)
            print("{0} is even, so I take half: {1}".format(input,response))
            counter += 1
        else:
            response = float(3*input) + 1
            print("{0}  is odd, so I make 3n+1: {1}".format(input,response))
            counter += 1
        input = response

    print("It took {0} steps to reach 1".format(counter))

if __name__ == '__main__':
    main(input, counter)
