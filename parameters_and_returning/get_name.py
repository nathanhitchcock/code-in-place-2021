def get_name():
    name = input("what's your name?")
    
    return name

def main():
    name = get_name() # get_name() will return a string which we store to the 'name' variable here
    print("Howdy", name, "! 🤠")

if __name__ == "__main__":
    main()
