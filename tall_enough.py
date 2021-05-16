'''
Tall enough to ride
Write a program which asks the user how tall they are and 
prints whether or not they're taller than a pre-specified minimum height.

In amusement parks (ah, the good old pre-pandemic days...), 
rollercoasters frequently have minimum height requirements for safety reasons.  
Assume for now that the minimum height is 50 of whatever height unit you'd like :)
'''

def main():
    height = input("How tall are you? ")
    height = int(height)

    if (height > 50):
        print("You're tall enough to ride!")
    else:
        print("I'm sorry you're too short to ride!")

if __name__ == "__main__":
    main()
