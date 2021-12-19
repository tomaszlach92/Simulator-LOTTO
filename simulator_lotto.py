from random import randint


def guess_the_number():
    """Function with game."""
    guess = False
    number = randint(1, 100)
    while not guess:
        try:
            user_number = float(input("Guess the number:"))
            if number == user_number:
                guess = True
                print("You win!")
            elif number < user_number:
                print("To big!")
            elif number > user_number:
                print("To small!")
        except ValueError:
            print("It's not a number!")


if __name__ == '__main__': guess_the_number()
