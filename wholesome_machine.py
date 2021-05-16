'''
Wholesome machine
Write a program which prompts the user to type an affirmation of your choice 
(we'll use "I am capable of doing anything I put my mind to.") 
until they type it correctly. Sometimes, especially in the midst of such 
uncertain times, we just need to be reminded that we are 
resilient, capable, and strong; this little Python program may be able to help!
'''
# setting the global prompt & affirmation variables so they are easier to work with
prompt = "Please type the following affirmation: "
affirmation = "I am capable of doing anything I put my mind to."

def main():     
    # we set up the scene by asking the prompt and setting the affirmation 
    print(prompt + affirmation)
    user_input = input()

    # we compare the user's input to the set affirmation
    while(user_input != affirmation):
        # if the user's input does not match, we loop the input
        print("That was not the affirmation.")
        print(prompt + affirmation)
        user_input = input()
    
    # once the input matches, we praise them! 
    print("That's right! :)")



if __name__ == "__main__":
    main()
