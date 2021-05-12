def main():
    DOG_YEARS = float(7.18)

    # collect the user's age
    human_age = input("Enter an age in human years: ")
    human_age = float(human_age)

    # calculate equivalent in dog years
    result = calculate_dog_years(human_age, DOG_YEARS)
    print("That's " + str(result) + " in dog years!")

def calculate_dog_years(human_age, DOG_YEARS):
    return human_age * DOG_YEARS






if __name__ == "__main__":
    main()
