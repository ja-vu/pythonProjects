import random
import string

min_length = 6





def start():
    # Ask user how long he wants his password to be
    pass_length = int(input("How long of a password do you want?"))

    # Password must be a min of 6 characters

    if pass_length < min_length:
        print("Your password must have atleast {0} characters".format(min_length))

    res = ''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation, k = pass_length))
    print(res)
## Have a mix of upper and lower as well as numbers and symbols


if __name__ == "__main__":
    start()