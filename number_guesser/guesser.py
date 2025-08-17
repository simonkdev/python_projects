from random import randint

def check_guess(guess, number):
    if guess < number:
        print("Too low!")
        return False
    elif guess > number:
        print("Too high!")
        return False
    else:
        print("Congratulations! You've guessed the number!")
        return True

def new_guess():
    guess = input("Guess a number between 0 and 100: ")
    if guess.isdigit():
        guess = int(guess)
    if 0 <= guess <= 100:
        return guess
    else:
        print("Please enter a number between 0 and 100.")
        return None
    

print("Welcome! Let's play a number guessing game!")


while True: 
    x = randint(0, 100)
    print("I have selected a number between 0 and 100. Try to guess it!")
    guess = new_guess()
    while guess is None or not check_guess(guess, x):
        guess = new_guess()
    play_again = input("Do you want to play again? (y/n): ").strip().lower()
    if play_again != 'y' or play_again != 'yes' or play_again != 'yes please' or play_again != 'ye':
        print("Thanks for playing, Goodbye!")
        break
