from random_word import RandomWords

# Create guess the word game
GUESS_WORD = []
SECRET_WORD = RandomWords()
SECRET_WORD = SECRET_WORD.get_random_word()
LENGTH_OF_WORD = len(SECRET_WORD)


def print_word_to_guess():
    """Utility function to print the current word to guess"""
    print("\n" + 10 * "======")
    print("Hello! Welcome to a game of Hangman!\n")
    print("The random word has..." + str(LENGTH_OF_WORD) + " characters!")

    for _ in SECRET_WORD:
        GUESS_WORD.append("-")
    print(GUESS_WORD)


# User needs to be able input letter guesses
def guess_word(secret_word, tries_left):
    used_letters = ""

    # Number of turns that the user has:
    print("\nInstructions:")
    print("You have " + str(tries_left) + " tries to guess the word!")
    print("Be aware that You can enter only 1 letter from a-z")
    print(10*"======"+"\n")

    # While user has tries left
    while tries_left != 0:
        answer = input("Please enter a letter: \n").lower()

        # Restrict user to only a single letter
        while len(answer) != 1:
            answer = input("Please enter a single letter: \n").lower()

        # If user guessed the right letter
        if answer in secret_word:
            print(10*"======")
            print("\n***** You have guessed correctly! *****\n")

            # If its a duplicate letter
            if answer in used_letters:
                continue

            # If its a new letter, add it to the list of used letters
            else:
                used_letters += answer + " "

            for x in range(0, len(secret_word)):
                if secret_word[x] == answer:
                    GUESS_WORD[x] = secret_word[x]
            print(GUESS_WORD)
            print("Used letters: " + used_letters+"\n")

            if list(SECRET_WORD) == GUESS_WORD:
                print("***** GOOD JOB! YOU HAVE WON *****")
                break
            else:
                print("Guess another character!")

        else:
            print(10*"======")
            print("\nWrong! Try another letter!")
            tries_left -= 1
            print("You have " + str(tries_left) + " tries left!\n")
            print(GUESS_WORD)

            if answer in used_letters:
                continue
            else:
                used_letters += answer + " "
            print("Used letters: " + used_letters+"\n")
            if tries_left == 0:
                print("Game Over! You have used up all your chances. Better luck next time!")
                break


if __name__ == "__main__":
    print_word_to_guess()
    guess_word(SECRET_WORD, 10)

# A limit should also be set on how many guesses they can use

# Keep notifying the user of the remaining turns
