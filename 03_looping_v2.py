# Error with loops not counting up and rounds looping every guess

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
    
# Main Routine goes here
# Constants for program
secret_num = 25
choose_instruction = "Please Guess a Number: "

# Ask user for # of rounds, <enter> for infinite mode
rounds = check_rounds()

# Main Rounds Loop
end_game = "no"
while end_game == "no":

    # Constants for loop
    guesses_played = 0
    guesses_allowed = 10
    rounds_played = 0

    # Rounds Heading
    print()
    if rounds == "":
        heading = f"Continous Mode: Round {rounds_played + 1}"
        
    else:
        heading = f"Round {rounds_played + 1} of {rounds}"
        
    print(heading)

    # Secondary Rounds Loop (For allowed guesses of each round)    
    end_round = "no"
    while end_round == "no":

        print("guess")

        end_round = "yes"

        # This will be Main Game Code (Finish Later)
        guess_heading = f"Guess {guesses_played + 1} of {guesses_allowed}"

        print(guess_heading)

    # Temporary Here
        guess = int_checker("Please choose a number between 1 & 26: ", 1, 26)

        # Too High or Low Checker
        if guess < secret_num:
            print("Too Low")

        elif guess > secret_num:
            print("Too High")

        elif guess == secret_num:
            print("Well Done")
            break
    # Till Here

        # End game if exit code is typed
        if guess == "xxx":
            break

        # Rest of loop / round
        guesses_played += 1

        if guesses_played == guesses_allowed:
            end_round = "yes"

    # Rest of loop / game
    rounds_played += 1
    
    if rounds_played == rounds:
            end_game = "yes"