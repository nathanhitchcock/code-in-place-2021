DAYS_IN_YEAR = 365
HOURS_IN_DAY = 24
MINS_IN_HOUR = 60
SECS_PER_MIN = 60

def main():
    seconds_in_year()
    print_result(result)

def seconds_in_year():
    global result
    result = DAYS_IN_YEAR * HOURS_IN_DAY * MINS_IN_HOUR * SECS_PER_MIN
    return(result)

def print_result(result):
    print("There are " + str(result) + " seconds per year")

if __name__ == "__main__":
    main()
