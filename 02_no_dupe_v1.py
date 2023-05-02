# Main Routine
# Constants for program
secret_num = 7     # Will be randomly generated (Replace later)
guesses_allowed = 5    # Will be calculated (Replace later)

guesses_left = guesses_allowed
num_won = 0

guess = ""

# Lists for program
already_guessed = []

while guess != secret_num and guesses_left >= 1:

    guess = int(input("Guess: "))   # Replace with int_checker

    # Checks that guess is not duplicate
    if guess in already_guessed:
        print(f"You have already guessed that number!",
              "You have {guesses_left} guesses left, please try again: ")
        continue
    
    guesses_left -= 1
    # Append every guess to list
    already_guessed.append(guess)
    
    # From here down will be changed later
    if guess < secret_num:
        print("Too Low")

    elif guess > secret_num:
        print("Too High")

if guess == secret_num:
    print("Well Done")

else:
    print("You have run out of rounds")
