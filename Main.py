"""Sprint Integration Project.

This program demonstrates Python fundamentals including arithmetic operations,
string handling, loops, input validation, and basic game logic in PEP 8 style.
"""
__author__ = "Sergio Beristain Cruz"

# 'import' allows you to use predefined functions from external Python modules
import time  # Used to pause the program via time.sleep()
import random  # Used to generate random numbers via random.randint()


def exponentiation_calculation(number_input1, number_input2):
    """Returns and print the exponentiation of two integers."""
    result = number_input1 ** number_input2
    # The double asterisks "**" serves as an exponent operator, like finding
    # the power of a number.
    print(f"\nExponentiation.\n"
          f"{number_input1} raised to the power of {number_input2} "
          f"returns {result}")


def multiplication_calculation(number_input1, number_input2):
    """Prints the product of two numbers."""
    # The single asterisk "*" serves as the multiplication symbol.
    result = number_input1 * number_input2
    print(f"\nMultiplication.\n"
          f"{number_input1} multiplied by {number_input2} returns {result}")


def division_calculation(number_input1, number_input2):
    """Prints the quotient of dividing one number by another."""
    # The slash "/" serves as the division symbol.
    result = number_input1 / number_input2
    print(f"\nDivision.\n"
          f"{number_input1} divided by {number_input2} returns {result}")


def remainder_calculation(number_input1, number_input2):
    """Prints the remainder of dividing one number by another."""
    # The percent "%" serves as the modulo symbol, returning the remainder
    # after division.
    result = number_input1 % number_input2
    print(f"\nReminder.\n"
          f"{number_input1} divided by {number_input2} returns a remainder "
          f"of {result}")


def floor_division_calculation(number_input1, number_input2):
    """Prints the floor-division result of two numbers."""
    # The double slash "//" serves as the floor division symbol, rounding
    # down the result.
    result = number_input1 // number_input2
    print(f"\nFloor Division.\n"
          f"{number_input1} divided by {number_input2} returns a value "
          f"rounded down to the nearest number being {result}")


def addition_calculation(number_input1, number_input2):
    """Prints the sum of two numbers."""
    # The plus "+" serves as the addition symbol.
    result = number_input1 + number_input2
    print(f"\nAddition.\n"
          f"{number_input1} added by {number_input2} returns {result}")


def subtraction_calculation(number_input1, number_input2):
    """Prints the difference when one number is subtracted from another."""
    # The minus "-" serves as the subtraction symbol.
    result = number_input1 - number_input2
    print(f"\nSubtraction.\n"
          f"{number_input1} subtracted by {number_input2} returns {result}")


def shortcut_operators(number_input1, number_input2):
    """
    Demonstrates Python shortcut operators.

    Prints the results by applying +=, -=, *=, /=, //=, and %=
    using the provided numbers.
    """
    original_a = number_input1  # Here we save the original variable of 'a'
    # under 'original_a' to ensure calculations are properly performed based
    # on the users two inputs and not the results of previous equations.

    a = original_a
    b = number_input2

    a += b
    print(f"a += b returns {a}")
    a = original_a
    a -= b
    print(f"a -= b returns {a}")
    a = original_a
    a *= b
    print(f"a *= b returns {a}")
    a = original_a
    a /= b
    print(f"a /= b returns {a}")
    a = original_a
    a //= b
    print(f"a //= b returns {a}")
    a = original_a
    a %= b
    print(f"a %= b returns {a}")


def string_repetition(string_input, number_input):
    """Prints the result of repeating a string a specified number of times."""
    print(f"{string_input} multiplied by {number_input} returns: ",
          string_input * number_input, sep='')
    # In print, a word is being multiplied based on the input variable which
    # ends up repeating the word. sep='' removes the double-spacing from
    # between returns: and the added space created via using "," to unify
    # the string and operation.


def string_concatenation(string_input1, string_input2):
    """Prints the result of concatenating two strings."""
    print(f"{string_input1} added by {string_input2} returns:",
          string_input1 + string_input2)
    # In the print, two words are being added to each other which is called
    # concatenation. end=" " unifies two separate lines into one and can
    # create spacing between those strings or remove them, you can also add
    # end="-" to add a dash between the strings.


# A function that prints a numerical triangle based on the parameter "height"
def output_triangle(height):
    """
    Prints a numerical triangle pattern based on height.

    Each row contains repeated digits equal to the row number.
    """
    for row in range(1, height + 1):
        for column in range(row):
            print(row, end=" ")
        print()


# A function that rolls a dice based on the parameter 'number_of_rolls' and
# returns the total number accumulated
def roll_dice(number_of_rolls):
    """
    Rolls a six-sided die a specified number of times.

    Returns the total sum of all dice rolls.
    """
    total = 0
    for rolls in range(number_of_rolls):
        total += random.randint(1, 6)
    return total


def main():
    print("\nGreetings, and welcome to the showcase of my Python progression "
          "journey!")
    time.sleep(3)
    print(
        "Throughout this program, you will be entering specific inputs based "
        "on the prompts direction.\n")
    time.sleep(3)

    valid_input = False
    program_execution = ""

    while not valid_input:
        program_execution = input("Enter y to start or n to quit.\n")

        if program_execution == "y" or program_execution == "n":
            valid_input = True
        else:
            print("\nError: Invalid input. Please enter 'y' or 'n'.\n")

    # 'while' is a type of loop that repeats the code inside it and repeats
    # itself as long as the condition is True. In this case, it also uses 'and'
    # to ensure the loop runs while the string input 'n' is not entered.
    while program_execution == "y" and program_execution != "n":

        print(
            "You will now be asked to enter two numbers which will perform "
            "a series of mathematical operations all at once.")
        time.sleep(2)
        num_input1 = 0
        num_input2 = 0
        math_section = False
        while not math_section:
            try:
                num_input1 = int(input("Enter the first number.\n"))
                num_input2 = int(input("Enter the second number.\n"))

                if num_input2 == 0:
                    print(
                        "\nError: '0' does not allow for proper calculations, "
                        "try again!")
                else:
                    math_section = True
            except ValueError:
                print("Error: Invalid input. Please enter whole numbers only!")

        exponentiation_calculation(num_input1, num_input2)
        multiplication_calculation(num_input1, num_input2)
        division_calculation(num_input1, num_input2)
        remainder_calculation(num_input1, num_input2)
        floor_division_calculation(num_input1, num_input2)
        addition_calculation(num_input1, num_input2)
        subtraction_calculation(num_input1, num_input2)

        # Shortcut Operators perform mathematical operations in the shortest
        # way possible.
        print(
            "\nHere is a shortcut operator demo that preforms most of the "
            "equations as seen previously but in a more efficient manner. ")
        a = 0
        b = 0
        math_section2 = False
        while not math_section2:
            try:
                a = int(input("Enter an int number: "))
                b = int(input("Enter another int number: \n"))
            except ValueError:
                print("Error: Invalid input. Please enter whole numbers only!")
                continue

            if b == 0:
                print("\nError: '0' does not allow for proper calculations, "
                      "try again!")
                continue
            math_section2 = True
        shortcut_operators(a, b)

        string_input_repetition = ""
        number_input_repetition = 0
        string_section1 = False
        while not string_section1:
            try:
                string_input_repetition = input(
                    "\nString Repetition.\nEnter a word: ")
                number_input_repetition = int(input("Enter an int number: "))
            except ValueError:
                print(
                    "Error: Invalid input. Please enter a value as prompted!")
                continue

            if number_input_repetition < 0:
                print("Error: Invalid input. "
                      "Please enter a number greater than 0!")
                continue
            string_section1 = True
        string_repetition(string_input_repetition, number_input_repetition)

        print("\nString", end=" ")
        print("Concatenation")
        string_input_add1 = ""
        string_input_add2 = ""
        string_section2 = False
        while not string_section2:
            try:
                string_input_add1 = input("Enter a word: ")
                string_input_add2 = input("Enter another word: ")
            except ValueError:
                print("Error: Invalid input. Please enter letters only!")
                continue
            string_section2 = True
        string_concatenation(string_input_add1, string_input_add2)

        print("\nLet's make a triangle!")
        triangle_height = 0
        math_section3 = False
        while not math_section3:
            try:
                triangle_height = int(input("Enter an int number: "))
            except ValueError:
                print("Error: Invalid input. Please enter whole numbers only!")
                continue

            if triangle_height <= 0:
                print(
                    "Error: Triangle height must be a positive number greater "
                    "than 0.!")
                continue
            math_section3 = True
        output_triangle(triangle_height)

        print("\nLet's play a game!")
        print(
            "You will be rolling a dice any number of times you desire.\nYour "
            "goal is to reach a range between 50-60 points in one go!\nKeep "
            "rolling until that range is reached!.")

        game_won = False
        while not game_won:  # Repeats the program forever via 'True'
            try:
                roll_count = int(input(
                    "Enter the number of rolls you wish to use: "
                ))
            except ValueError:
                print("Error: Invalid input. Please enter whole numbers only!")
                continue
            total_points = roll_dice(roll_count)

            # 'if' executes the code inside only if the condition is True.
            # 'else' executes its block only if the previous conditions like
            # 'if' and 'elif' return false (elif is the same as if and allows
            # for more conditional checking blocks)
            if total_points < 50 or total_points > 60:
                print("\nYou rolled a total of", total_points,
                      "points. Try again!")
                continue  # 'continue' keeps the while loop functioning and
                # continues to repeat itself unless told otherwise.
            else:
                print("\nYou rolled a total of", total_points,
                      "points. You reached the range goal! "
                      "Thanks for playing!!")
                game_won = True

        program_execution = ""
        restart_program_section = False
        while not restart_program_section:
            try:
                program_execution = input(
                    "\nEnter y to restart the program or n to quit\n")
                if program_execution != "y" and program_execution != "n":
                    raise ValueError
            except ValueError:
                print("Error: Invalid input. Please enter 'y' or 'n'.")
                continue
            restart_program_section = True

        if program_execution == "y":
            print("Restarting the program...")
            time.sleep(3)
        else:
            print("terminating program...")
            time.sleep(3)

    print("\nThank you for going through my Python Fundamentals showcase.")
    time.sleep(3)


if __name__ == "__main__":
    main()
