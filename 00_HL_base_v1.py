import random
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

def check_rounds():
    while True:
        response = int_checker("How Many Rounds: ", 1)

        round_error = "Please type either <enter> or an integer that is more than 0"

        if response != "":
            try:
                response = int(response)

                if response < 1:
                    print(round_error)
                    continue

            except ValueError:
                print(round_error)
                continue

        return response
  
def statement_deco(deco_sides, deco_top_bottom, start_statement, three_line):
    # Sets up decoration for sides of statement and top / bottom
    sides = deco_sides * 3
    single_statement = f"{sides} {start_statement} {sides}"

    top_bottom = deco_top_bottom * len(single_statement)
    big_statement = f"{top_bottom}\n{single_statement}\n{top_bottom}"

    # Outputs either single or triple line statement
    if three_line == 1:
        return single_statement

    elif three_line ==3:
        return big_statement

def instructions():
    intro = statement_deco("*", "-", "How To Play", 1)
    print(intro)
    print("Playing Higher Lower is fairly simple")
    print("All you have to do is choose a range of numbers that the program will choose a random 'Secret' number from")
    print("You give it a 'Low Number' that can be any Whole Number, 0 or higher, then you give it a 'High Number' that is atleast 1 more than the 'Low Number'")
    print("Then you choose a Number of Rounds to Play with that range (It will choose a new number every round)")
    print("I Can't Be Bothered To Write Anymore Instruction")
    return ""

# Main Routine goes here
# Constants for program
rounds_played = 0
choose_instruction = "Please Guess a Number: "

# Lists or Dicts for program
yes_no_list = ["yes", "no"]

# Welcome to game statement
welcome_statement = statement_deco("=", "-", "Welcome to The Higher Lower Game", 3)
print(welcome_statement)

# Ask user if they have played before
played_before = choice_checker("Have you played The Higher Lower Game before? ", "Please answer 'Yes' or 'No'", yes_no_list)

# If 'yes', show instructions
if played_before == "no" or played_before == "n":
    print()
    print(instructions())

else:
    print()

# Play Game again loop
play_again = "yes"
while play_again == "yes":

    # Now play the game
    print("Now to actually play the game")
    print()

    # Ask user for Low # (for secret # range)
    low_num = int_checker("Low Number: ")

    # Ask user for High # (for secret # range)
    high_num = int_checker("High Number: ", low_num + 1)

    # Generate max allowed guesses
    range = high_num - low_num + 1
    max_raw = math.log2(range)
    max_upped = math.ceil(max_raw)
    max_guesses = max_upped + 1   

    # Ask user for # of rounds, <enter> for infinite mode
    rounds = int_checker("How Many Rounds? <Enter for Infinite> ", 1, exit_code="")

    # Main Rounds Loop
    end_round = "no"
    while end_round == "no":
        
        # Constants for loop
        guesses_played = 0
        guesses_left = 2

        # Lists for loop
        already_guessed = []

        # Generate random 'secret' number
        secret_num = random.randint(low_num, high_num)

        # Rounds Heading
        print()
        if rounds == "":
            heading = f"Continous Mode: Round {rounds_played + 1}"
            
        else:
            heading = f"Round {rounds_played + 1} of {rounds}"
            
        print(heading)

        # Secondary Rounds Loop (For allowed guesses of each round)    
        end_guess = "no"
        while end_guess == "no":

            # This will be Main Game Code (Finish Later)
            guess_heading = f"Guess {guesses_played + 1} of {max_guesses}"

            print(guess_heading)

            # Checks intput is 
            guess_question = f"Please choose a number between {low_num} & {high_num}: "
            guess = int_checker(guess_question, low_num, high_num, "xxx")

            # Checks that guess is not duplicate
            if guess in already_guessed:
                print("You have already guessed that number!",
                    f"\nYou have {guesses_left} guesses left, please try again: ")
                guesses_left -= 1

            # Else append every guess to list
            else:
                already_guessed.append(guess)
            
            # End game if exit code is typed
            if guess == "xxx":
                end_round = "yes"
                break

            # Too High or Low Checker
            if guess < secret_num:
                print("Too Low")

            elif guess > secret_num:
                print("Too High")

            elif guess == secret_num:
                print("Well Done")
                break

            # Empty Print for spacing
            print()

            # Rest of loop / round
            guesses_played += 1

            if guesses_played == max_guesses:
                end_guess = "yes"

        # Rest of loop / game
        rounds_played += 1
        
        if rounds_played == rounds:
                end_round = "yes"

    # Tell user they have run out of rounds to play
    print()
    print("You have Finished Playing the Rounds you asked for")
    
    # Ask user if they want to play again
    ask_play_again = choice_checker("Do you want to play again? ", "Please answer 'Yes' or 'No'", yes_no_list)
    if ask_play_again == "no" or ask_play_again == "n":
        play_again = "no"
    
    # Print empty line for looks
    print()

# Thanks for Playing statement
thanks_playing_statement = statement_deco("!", "-", "Thanks For Playing The Higher Lower Game", 3)
print(thanks_playing_statement)