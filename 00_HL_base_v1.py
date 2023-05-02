# Functions go here
def int_checker(question, low=None, high=None):
    # Constant for function
    situation = ""

    # Sets variable for type of integer checking
    if low is not None and high is not None:
        situation = "both"

    elif low is not None and high is None:
        situation = "low only"

    while True:

        try:
            response = int(input(question))

            # Checks input is not too high or too low, if specified
            if situation == "both":
                if response < low or response > high:
                    print(f"Please enter a number between {low} and {high}")
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

def choice_checker(question, error, valid_list):
    valid = False
    while not valid:
        # Ask user for choice (and force lowercase)
        response = input(question).lower()

        # Runs through list and if response is an item in list (or first letter), the full name is returned
        for item in valid_list:
            if response == item[0] or response == item:
                return response

        # Output error if response not in list        
        print(error)
        print()






# Main Routine goes here
# Constants for program


# Lists or Dicts for program


# Welcome to game statement


# Ask user if they have played before


# If 'yes', show instructions


    # Ask user for Low # (for secret # range)


    # Ask user for High # (for secret # range)


    # Generate 'secret' # between Low # and High #


    # Calculate allowed guesses for secret # range


    # Ask user for # of rounds, <enter> for infinites


        # Rounds Headings (Round # of # or Continous Mode: Round #)


        # Ask user for # to guess


        # Compare user guess to 'secret' #


        # If user guess is 'secret' #, end round


    # Tell user they have run out of rounds to play


# Ask user if they want to play again


# Thanks for Playing statement