from random import randint

LOW = 0
HIGH = 100


def random_number_generator():
    rand_num = randint(LOW, HIGH)
    return rand_num


def ask_user():
    hidden_number = int(random_number_generator())

    while True:
        try:
            guess = int(input("Guess a number between: {0} and {1}".format(LOW, HIGH)))
        except ValueError:
            print("Please enter a number")
            continue

        if guess == hidden_number:
            print("YOU HAVE GOT IT!!!")
            break
        elif guess > HIGH or guess < LOW:
            print("Please keep your guess between {0} and {1}".format(LOW, HIGH))

        elif guess > hidden_number:
            print("Number is lower")

        elif guess < hidden_number:
            print("Number is higher")


if __name__ == "__main__":
    ask_user()
