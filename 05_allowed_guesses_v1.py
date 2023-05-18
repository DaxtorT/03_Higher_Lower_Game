import math

# Functions go here
def int_checker(question, low=None, high=None, exit_code=None):
    # Constant for function
    situation = ""

    # Sets variable for type of integer checking
    if low is not None and high is not None:
        situation = "both"

    elif low is not None and high is None:
        situation = "low only"

    while True:

        response = input(question)
        if response == exit_code:
            return response

        try:
            response = int(response)

            # Checks input is not too high or too low, if specified
            if situation == "both":
                if response < low or response > high:
                    print(f"Please enter a number between {low} and {high} (Inclusive)")
                    continue

            # Checks input is not too low
            elif situation == "low only":
                if response < low:
                    print(f"Please enter a number that is more than (or equal to) {low}")
                    continue

            return response

        # Checks input is an integer
        except ValueError:
            print("Please enter an integer")
            continue

# Main Routine goes here
#  Temp
play_again = "yes"
while play_again == "yes":
    # Ask user for low and high number for secret num to be in
    low_num = int_checker("Low Number: ")
    high_num = int_checker("High Number: ", low_num + 1)

    # Allowed guess calculations go here
    range = high_num - low_num + 1
    max_raw = math.log2(range)
    max_upped = math.ceil(max_raw)
    max_guesses = max_upped + 1
    print(f"Max Guesses: {max_guesses}")

    # Temp loop for testing
    play_again = input("Again? ")
