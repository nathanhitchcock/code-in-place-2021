def print_divisors(num):
    i = 1
    # iterate over the possible numbers, starting with 1 and going to the target
    # printing those that don't have a remainder
    while i <= num :
        if (num % i==0) :
            print(i)
        i = i + 1

    return num

def main():
    num = int(input("Enter a number: "))
    print_divisors(num)

if __name__ == "__main__":
    main()
