from random import randint

min_val = 1
max_val = 6


# Dice needs to return a random value between 1 and 6
def roll_dice(low, high):
    print(randint(low, high))


def start():
    """ ASK USER IF THEY WANT TO ROLL A DICE """
    roll_again = True
    while roll_again:
        roll_dice(min_val, max_val)
        print("Do you want to re-roll? Y/N")
        roll_again = "Y" in input().upper()


if __name__ == "__main__":
    start()
