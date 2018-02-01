"""
### CODEBREAKER 9000 ###
"""

import random

WELCOME_MSG = "Welcome, fellow code breaker! Let's see if you can guess my 3 digit number.\n\
Each digit only appears once in the number.\n\
Type 'I give up' to exit in case you give up."
USER_LEAVE_MSG = "Poor you. The number was {number_to_guess}. Good luck next time."
CODE_GENERATED_MSG = "The code has been generated."
MAKE_NEXT_GUESS_MSG = "What is your guess?\n"
ERROR_WRONG_INPUT_TYPE_MSG = "That's not an integer. Only 3-digit integers are allowed."
ERROR_INPUT_IN_WRONG_RANGE_MSG = "This is not a 3-digit integer. Only 3-digit integers are allowed."
MATCH_MSG = "At least {number_of_correct_digits} of your digits {is_or_are} correct and \
{has_or_have} the correct position."
CLOSE_MSG = "At least {number_of_correct_digits} of your digits {is_or_are} correct and \
{has_or_have} wrong position."
FAIL_MSG = "None of your digits are correct."
# plural_fix should be either "s" or an empty string, depending on the number_of_attempts
SUCCESS_MSG = "Great! You finally made it and it only took you as little as {number_of_attempts} \
attempt{plural_fix}."


def main_game_func():
    """
    Calls subroutines to initialize the game, process user input and react to it.
    """

    initialize()
    number_to_guess = generate_number_to_be_guessed()
    notify_on_code_generation()
    attempts_counter = process_input_loop(number_to_guess)
    # In case of giving up attempts_counter is set to zero. No congratulations for leavers.
    if attempts_counter > 0:
        congratulate_winner(attempts_counter)


def initialize():
    """
    Welcomes user.
    """

    print(WELCOME_MSG)


def generate_number_to_be_guessed():
    """
    Generates random 3-digit number with only one occurence of each digit.
    The result is returned as a string.
    """

    digits = [str(digit) for digit in range(10)]
    random.shuffle(digits)

    return ''.join(digits[:3])


def notify_on_code_generation():
    """
    Notifies user of successful code generation.
    """

    print(CODE_GENERATED_MSG)


def process_input_loop(number_to_guess):
    """
    Processes user input to count attempts and give unlucky users clues.
    Upon leaving attempts_counter is reset to zero.
    """

    attempts_counter = 0
    while True:
        user_attempt = input(MAKE_NEXT_GUESS_MSG)
        # If user gave up, break the loop to return attempts_counter.
        if user_attempt.lower() == "I give up".lower():
            process_exit(number_to_guess)
            attempts_counter = 0
            break

        attempts_counter += 1
        if verify_input(user_attempt):
            # If user has guessed, break the loop to return attempts_counter.
            if user_has_guessed(number_to_guess, user_attempt):
                break
            # Only give clues if input was verified.
            else:
                give_clue(number_to_guess, user_attempt)

    return attempts_counter


def verify_input(guess):
    """
    Verifies user input against type and magnitude.
    Returns zero in case of error, otherwise casts input string to integer
    and returns it.
    """

    try:
        guess_int = int(guess)
    except ValueError:
        print(ERROR_WRONG_INPUT_TYPE_MSG)
        return False

    if guess_int < 100 or guess_int > 999:
        print(ERROR_INPUT_IN_WRONG_RANGE_MSG)
        return False
    else:
        return True


def user_has_guessed(number_to_guess, guess):
    """
    Verifies user input (string expected) against the generated code (string expected).
    """

    return number_to_guess == guess


def give_clue(number_to_guess, user_attempt):
    """
    Gives unlucky users a clue about their life.
    """

    number_to_guess_str = str(number_to_guess)

    # Correct digit is present and is in the correct position.
    correct_digits_counter = 0
    # Correct digit is present, though the position is wrong.
    guessed_digits_counter = 0

    for i in range(3):
        if user_attempt[i] == number_to_guess_str[i]:
            correct_digits_counter += 1
        elif user_attempt[i] in number_to_guess_str:
            guessed_digits_counter += 1

    if correct_digits_counter > 0:
        if correct_digits_counter == 1:
            copula_one = 'is'
            copula_two = 'has'
        else:
            copula_one = 'are'
            copula_two = 'have'
        print(MATCH_MSG.format(
            number_of_correct_digits=correct_digits_counter,
            is_or_are=copula_one,
            has_or_have=copula_two))
    if guessed_digits_counter > 0:
        if guessed_digits_counter == 1:
            copula_one = 'is'
            copula_two = 'has'
        else:
            copula_one = 'are'
            copula_two = 'have'
        print(CLOSE_MSG.format(
            number_of_correct_digits=guessed_digits_counter,
            is_or_are=copula_one,
            has_or_have=copula_two))
    if correct_digits_counter == guessed_digits_counter == 0:
        print(FAIL_MSG)


def process_exit(number_to_guess):
    """
    Says farewell to unlucky users.
    """

    print(USER_LEAVE_MSG.format(number_to_guess=number_to_guess))


def congratulate_winner(attempts_counter):
    """
    Congratulates winner.
    """

    plural_fix = ""
    if attempts_counter > 1:
        plural_fix = "s"

    print(SUCCESS_MSG.format(
        number_of_attempts=attempts_counter, plural_fix=plural_fix))


main_game_func()
