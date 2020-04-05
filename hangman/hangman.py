import random

# Create guess the word game
WORD_LIST = ['apple', 'banana', 'bumblebee', 'caterpillar', 'zebra']
GUESS_WORD = []
SECRET_WORD = random.choice(WORD_LIST)
LENGTH_OF_WORD = len(SECRET_WORD)
ALPHABET = "abcdefghijklmnopqrstuvwxyz"
letter_storage = []


def print_word_to_guess():
    """Utility function to print the current word to guess"""
    print("\n" + 10 * "======")
    print("Hello! Welcome to a game of Hangman!\n")
    print("The random word has..." + str(LENGTH_OF_WORD) + " characters!")

    for _ in SECRET_WORD:
        GUESS_WORD.append("-")
    print(GUESS_WORD)


def print_guesses_left(current: int, total: int):
    """Prints how many chances the player has left"""
    print("You are on guess {0}/{1}".format(current, total))


# User needs to be able input letter guesses
def guess_word(secret_word):
    guess_taken = 1
    max_guess = 10

    # Number of turns that the user has:
    print("\nInstructions:")
    print("Be aware that You can enter only 1 letter from a-z")
    print(10 * "======" + "\n")

    # While user has tries left
    while guess_taken < max_guess:
        answer = input("Please enter a letter: \n").lower()

        # Restrict user to only a single letter
        if answer not in ALPHABET:
            print("Enter a letter from a-z ALPHABET")
        elif answer in letter_storage:
            print("You have already used this letter!")
        else:
            letter_storage.append(answer)
        # If user guessed the right letter
            if answer in secret_word:
                print(10 * "======")
                print("\n***** You have guessed correctly! *****\n")

                for x in range(0, LENGTH_OF_WORD):
                    if secret_word[x] == answer:
                        GUESS_WORD[x] = secret_word[x]
                print(GUESS_WORD)

                if list(SECRET_WORD) == GUESS_WORD:
                    print("***** GOOD JOB! YOU HAVE WON *****")
                    break
            else:
                print(10 * "======")
                print("\nWrong! Try another letter!")
                guess_taken += 1
                print_guesses_left(guess_taken, max_guess)
                print(GUESS_WORD)
                if guess_taken == max_guess:
                    print("Game Over! You have used up all your chances. The secret word was: '" + SECRET_WORD + "'.Better luck next time!")
                    break


if __name__ == "__main__":
    print_word_to_guess()
    guess_word(SECRET_WORD)

