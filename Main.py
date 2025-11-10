"""Sprint Integration Project """
__author__ = "Sergio Beristain Cruz"

# 'import' allows you to use predefined functions from external Python modules
import time # Used to pause the program via time.sleep()
import random # Used to generate random numbers via math.randint()

# 'def' Defines a function that outputs a triangle based on the parameter,
# being height. def function (parameter)
def output_triangle(height):
    for row in range(1, height + 1):
        for column in range(row):
            print(row, end=" ")
        print()

# A function that rolls a dice based on the parameter 'number_of_rolls' and
# returns the total number accumulated
def roll_dice(number_of_rolls):
    total = 0
    for rolls in range(number_of_rolls):
        total += random.randint(1, 6)
    return total

print("\nGreetings, and welcome to the showcase of my Python progression "
      "journey!")
time.sleep(3)
print("Throughout this program, you will be entering specific inputs based "
      "on the prompts direction.\n")
time.sleep(3)

programExecution = input("Enter y to start or n to quit.\n")

# 'while' is a type of loop that repeats the code inside it and repeats
# itself as long as the condition is True. In this case, it also uses 'and'
# to ensure the loop runs while the string input 'n' is not entered.
while programExecution == "y" and programExecution != "n":

    numberInputPOW1 = int(input("Exponentiation.\nEnter an int number: "))
    numberInputPOW2 = int(input("Enter another int number: "))
    POWResult = numberInputPOW1 ** numberInputPOW2
    # The double asterisks "**" serves as an exponent operator, like finding the
    # power of a number.
    print(f"{numberInputPOW1} raised to the power of {numberInputPOW2} returns "
          f"{POWResult}")

    numberInputTimes1 = int(input("\nMultiplication.\nEnter an int number: "))
    numberInputTimes2 = int(input("Enter another int number: "))
    timesResult = numberInputTimes1 * numberInputTimes2
    # The single asterisk "*" multiples, like the two number variables shown above.
    print(f"{numberInputTimes1} multiplied by {numberInputTimes2} returns: "
          f"{timesResult}")

    numberInputDiv1 = int(input("\nDivision.\nEnter an int number: "))
    numberInputDiv2 = int(input("Enter another int number: "))
    divisionResult = numberInputDiv1 / numberInputDiv2
    # The slash sign "/" performs division as shown above.
    print(f"{numberInputDiv1} divided by {numberInputDiv2} returns: "
          f"{divisionResult}")

    numberInputRemainder1 = int(input("\nRemainder.\nEnter an int number: "))
    numberInputRemainder2 = int(input("Enter another int number: "))
    remainderResult = numberInputRemainder1 % numberInputRemainder2
    # The modulus operator "%" returns the remainder after dividing.
    print(f"{numberInputRemainder1} divided by {numberInputRemainder2} leaves a "
          f"reminder of {remainderResult}")

    numberInputFloor1 = int(input("\nFloor Division.\nEnter an int number: "))
    numberInputFloor2 = int(input("Enter another int number: "))
    floorResult = numberInputFloor1 // numberInputFloor2
    # Double slash signs "//" perform floor division which rounds down to the
    # nearest whole number.
    print(f"{numberInputFloor1} divided by {numberInputFloor2} rounds the result"
          f" down to the nearest whole number being {floorResult}")

    numberInputAdd1 = int(input("\nAddition.\nEnter an int number: "))
    numberInputAdd2 = int(input("Enter another int number: "))
    additionResult = numberInputAdd1 + numberInputAdd2
    # The plus sign "+" does addition.
    print(f"{numberInputAdd1} added by {numberInputAdd2} returns:"
          f" {additionResult}")

    numberInputMinus1 = int(input("\nSubtraction.\nEnter an int number: "))
    numberInputMinus2 = int(input("Enter another int number: "))
    minusResult = numberInputMinus1 - numberInputMinus2
    # The minus sign "-" does subtraction.
    print(f"{numberInputMinus1} subtracted by {numberInputMinus2} returns"
          f" {minusResult}")

    # Shortcut Operators perform mathematical operations in the shortest
    # way possible.
    print("\nHere is a shortcut operator demo that preforms most of "
          "the equations as seen previously but in a more efficient manner. ")
    a = int(input("Enter an int number: "))
    b = int(input("Enter another int number: "))

    original_a = a  # Here we save the original variable of 'a' under
                    # 'original_a' to ensure calculations are properly
                    # performed based on the users two inputs and not the
                    # results of previous equations.

    a = original_a
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

    stringInputRepetition = input("\nString Repetition.\nEnter a word: ")
    numberInputRepetition = int(input("Enter an int number: "))
    print(f"{stringInputRepetition} multiplied by {numberInputRepetition} "
          f"returns: ", stringInputRepetition * numberInputRepetition, sep='')
    # In the print, a word is being multiplied based on the input variable which
    # ends up repeating the word.
    # sep='' removes the double-spacing from between returns: and the added
    # space created via using "," to unify the string and operation.

    print("\nString", end=" ")
    print("Concatenation")
    stringInputAdd1 = input("Enter a word: ")
    numberInputAdd2 = input("Enter another word: ")
    print(f"{stringInputAdd1} added by {numberInputAdd2} returns:",
          stringInputAdd1 + numberInputAdd2)
    # In the print, two words are being added to each other which is called
    # concatenation.
    # end=" " unifies two separate lines into one and can create spacing between
    # those strings or remove them, you can also add end="-" to add a dash
    # between the strings.

    print("\nLet's make a triangle!")
    triangle_height = int(input("Enter an int number: "))
    output_triangle(triangle_height)

    print("\nLet's play a game!")
    print("You will be rolling a dice any number of times you desire.\nYour "
          "goal is to reach a range between 50-60 points in one go!\nKeep "
          "rolling until that range is reached!.")
    while True: # Repeats the program forever via 'True'
        roll_count = int(input("Enter the number of rolls you wish to use: "))
        total_points = roll_dice(roll_count)

        # 'if' executes the code inside only if the condition is True.
        # 'else' executes its block only if the previous conditions like
        # 'if' and 'elif' return false (elif is the same as if and allows for
        # more conditional checking blocks)
        if total_points < 50 or total_points > 60:
            print("\nYou rolled a total of", total_points,
                  "points. Try again!")
            continue  # 'continue' keeps the while loop functioning and
            # continues to repeat itself unless told otherwise.
        else:
            print("\nYou rolled a total of", total_points,
                  "points. You reached the range goal! Thanks for playing!!")
            break  # 'break' stops the while loop and exits out of it,
            # resuming the rest of the program.

    programExecution = input("\nEnter y to restart the program or n to quit\n")
    if programExecution == "y":
        print("Restarting the program...")
        time.sleep(3)
    elif not programExecution == "n":
        print("Invalid input.")
    else:
        print("Program terminated.")

print("\nThank you for going through my Python Fundamentals showcase.")
time.sleep(3)