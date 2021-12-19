from random import shuffle


def get_lotto_numbers():
    """Get numbers to lotto"""
    lotto_numbers = list(range(1, 49))
    shuffle(lotto_numbers)
    return lotto_numbers[:6]


LOTTO_NUMBERS = get_lotto_numbers()


def lotto(LOTTO_NUMBERS):
    """Function with lotto game."""
    user_numbers = input("Wprowadź 6 liczb w zakresie 1-49, oddzielając je spacją:")
    try:
        user_numbers_arr = user_numbers.split()
        numbers_int = [int(number) for number in user_numbers_arr]
        range_numbers = check_if_user_entered_correct_range_numbers(numbers_int)
        check_duplicates = check_if_duplicates(numbers_int)
        check_numbers_amount = check_if_user_entered_correct_amount_numbers(numbers_int)
        numbers_int.sort()
        LOTTO_NUMBERS.sort()
        amount_correct_numbers = how_many_is_correct(LOTTO_NUMBERS, numbers_int)

        user_numbers_str = [str(int) for int in numbers_int]
        user_numbers = ", ".join(user_numbers_str)
        lotto_str = [str(int) for int in LOTTO_NUMBERS]
        lotto_numbers = ", ".join(lotto_str)

        if not range_numbers:
            message = "Wprowadzone liczby nie mieszczą się w zakresie 1-49"
        elif check_duplicates:
            message = "Musisz wprowadzić 6 różnych liczb!"
        elif check_numbers_amount:
            message = "Nie wprowadziłeś odpowieniej ilości liczb!"
        else:
            message = f"""
Twoje liczby to: {user_numbers}.
Wylosowane liczby to: {lotto_numbers}.
Ilość trafień: {amount_correct_numbers}."""

        return message

    except ValueError:
        return "Nie wprowadzono 6 liczb!"


def check_if_user_entered_correct_range_numbers(user_numbers):
    """Check if given list elements has correct range"""
    i, j = 1, 49
    res = all(ele >= i and ele <= j for ele in user_numbers)
    return res


def check_if_user_entered_correct_amount_numbers(user_numbers):
    """Check if given list contains 6 elements"""
    if len(user_numbers) < 6 or len(user_numbers) > 6:
        return True
    return False


def check_if_duplicates(list_of_elems):
    """Check if given list contains any duplicates"""
    if len(list_of_elems) == len(set(list_of_elems)):
        return False
    return True


def how_many_is_correct(list_of_elems, second_list_of_elems):
    """Check how many numbers user guess"""
    test = set(list_of_elems) & set(second_list_of_elems)
    return len(test)


if __name__ == '__main__': print(lotto(LOTTO_NUMBERS))
