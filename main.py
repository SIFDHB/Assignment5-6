# Enables ansi escape characters in terminal
# https://stackoverflow.com/questions/12492810/python-how-can-i-make-the-ansi-escape-codes-to-work-also-in-windows
import os
os.system("")

# Constants
ANSI_ESCAPE = "\033[39m"

# ANSI escape codes for Minecraft colors
# https://minecraft.fandom.com/wiki/Formatting_codes
TEXT_COLORS = {
    'black': "\033[30m", 'dark_blue': "\033[34m", 'dark_green': "\033[32m", 'dark_aqua': "\033[36m",
    'dark_red': "\033[31m", 'dark_purple': "\033[35m", 'gold': "\033[33m", 'gray': "\033[37m",
    'dark_gray': "\033[90m", 'blue': "\033[94m", 'green': "\033[92m", 'aqua': "\033[96m",
    'red': "\033[91m", 'light_purple': "\033[95m", 'yellow': "\033[93m", 'white': "\033[97m",
}

# Applies colored text, using escape codes to the console.
def TextColor(text="", color="white", continuous=True):
    """
    Applies Color formatting to text using ANSI escape codes.

    :param text: The text to format.
    :param color: The color name (e.g., 'black', 'blue', 'green', etc.).
    :param continuous: Flag that implements ANSI_ESCAPE at the end of the string
    :returns: The formatted text.
    """

    # Check if the provided color is a valid color
    if color in TEXT_COLORS:
        return continuous and f"{TEXT_COLORS[color]}{text}{ANSI_ESCAPE}" or f"{TEXT_COLORS[color]}{text}"
    else:
        raise ValueError(f"Invalid color name: {color}")

# The Euclidean Algorithm
def EuclideanAlgorithm(a, b):
    """
    This function implements the Euclidean Algorithm to find the Greatest Common Divisor (GCD) of two integers.

    :param a: (int) First positive integer
    :param b: (int) Second positive integer

    :returns a: (int) GCD Result
    """

    # Loop until b becomes 0
    while b != 0:
        # Store current value of b
        temp = b
        # Set b to be the modulo of ab
        b = a % b
        # Set a to previous value of b
        a = temp
    # Return a as the GCD
    return a

def GetNumber(type):
    while True:
        try:
            result = int(input(f"Write down the {type} number: "))
            if result < 0:
                raise Exception("Invalid number. No negative numbers allowed.")
            return result
        except ValueError:
            print(TextColor("Invalid input. Please use positive integers only.", color="red"))
        except Exception as Error:
            print(TextColor(Error.args[0], color="red"))

a, b = GetNumber("first"), GetNumber("second")
gcd = EuclideanAlgorithm(a, b)
print(TextColor(f"The Greatest Common Divisor (GCD) of {a} and {b} is: ", "white") + TextColor(str(gcd), "yellow"))