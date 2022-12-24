#Auth : Sudip Chakrabarty
#The game is called a guessing game , where computer will randomly select a number from 1 to 100.
#You need to guess the number.

logo = """
 ______   __   __  _______  _______  _______  ___   __    _  _______      _______  _______  __   __  _______ 
|       ||  | |  ||       ||       ||       ||   | |  |  | ||       |    |       ||   _   ||  |_|  ||       |
|    ___||  | |  ||    ___||  _____||  _____||   | |   |_| ||    ___|    |    ___||  |_|  ||       ||    ___|
|   | __ |  |_|  ||   |___ | |_____ | |_____ |   | |       ||   | __     |   | __ |       ||       ||   |___ 
|   ||  ||       ||    ___||_____  ||_____  ||   | |  _    ||   ||  |    |   ||  ||       ||       ||    ___|
|   |_| ||       ||   |___  _____| | _____| ||   | | | |   ||   |_| |    |   |_| ||   _   || ||_|| ||   |___ 
|_______||_______||_______||_______||_______||___| |_|  |__||_______|    |_______||__| |__||_|   |_||_______|

"""

from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def check_answer(guess,answer,turns):
    """Checks answer against guess.Returns the number of turns remaining."""
    if guess > answer:
        print("too High")
        return turns - 1
    elif guess < answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got this!The answer was {answer}.")


def set_difficulty():
    level = input("which level do you want to play?For easy type 'easy'for hard type 'hard' : ") 
    if level == "easy" :
        return EASY_LEVEL_TURNS
    else :
        return HARD_LEVEL_TURNS


def game():
    print(logo)
    print("welcome to the number guessing game!") 
    print("I am thinking of a number between 1 to 100")
    print("You need to guess the number !")
    answer = randint(1,100)
    print(f"Pssat, the correct answer is {answer}")

    turns = set_difficulty()

    guess =0
    while guess != answer:
        print(f"You have {turns} attemps remaining to guess the number.")
        guess = int(input("Guess a number : "))
        

        turns = check_answer(guess,answer,turns)
        if turns == 0:
            print("You have run of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again.")

game()