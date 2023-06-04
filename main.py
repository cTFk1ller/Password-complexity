# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from argparse import ArgumentParser, Namespace
from pyfiglet import Figlet
from termcolor import colored


def readargs() -> Namespace:
    parser = ArgumentParser()
    parser.add_argument("-p", "--password", dest="password", help="mention the password you want to test", metavar="PASSWORD", required=True)
    parser.add_argument("-q", "--quiet", action="store_false", dest="verbose", default=True,
                        help="don't print status messages to stdout", required=False)
    arguments = parser.parse_args()
    return arguments
    pass


def print_hi(header):
    f = Figlet(font="fuzzy", width=180)
    welcome = colored(f.renderText(text=header), "yellow")
    if readargs().verbose is not False:
        print(f"\n{welcome}")
    pass


def printincolor(word, color='white'):
    print(colored(word, color))
    pass


# Define the variables to check complexity
lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
special_characters = "!@#$%^&*()_+-=[]{}|;:,.<>/?"


def test(password):
    complexity = 0
    if len(password) >= 8:
        complexity += 1
    if any(char in lowercase_letters for char in password):
        complexity += 1
    if any(char in uppercase_letters for char in password):
        complexity += 1
    if any(char in numbers for char in password):
        complexity += 1
    if any(char in special_characters for char in password):
        complexity += 1
    return complexity


if __name__ == '__main__':
    args = readargs()
    print_hi("Password's complexity script")
    printincolor("[*] The password should at least be 8 characters. consists of at least one lower and upper letter, number, and special character.", "blue")
    if args.password is not None:
        complexity = test(args.password)
        if complexity == 1:
            printincolor(f"[*] Weak password", "red")
        elif complexity == 2:
            printincolor("[*] Moderate password", "yellow")
        elif complexity == 3:
            printincolor("[*] Strong password, but still needs improvement.", "yellow")
        elif complexity == 4:
            printincolor("[*] Very strong password, you still can make better", "yellow")
        elif complexity == 5:
            printincolor("[*] Impossible to crack. well done", "green")

    printincolor("[*] Done", "blue")
    printincolor("\nMr.CTFKi11er", "red")
