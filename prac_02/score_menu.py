import random


def main():
    name = ""
    print("Menu: ")
    choice = input("> ").upper()
    while choice != "Q":
        if choice == "G":
            name = get_valid_name()
        elif choice == "P":
            print_greeting(name)
        elif choice == "S":
            print_secret_name(name)
        else:
            print("Invalid choice")
        print("Menu: ")
        choice = input("> ").upper()
    print("Farewell")


def print_greeting(name):
    length = len(name)
    print_line(length)
    print(name)
    print_line(length)


def get_valid_name():
    name = input("Enter your name: ")
    while name == "":
        print("Invalid name")
        name = input("Enter your name: ")
    return name


def print_line(length):
    print('-' * length)


def print_secret_name(name):
    letters = list(name)
    random.shuffle(letters)
    print("".join(letters))


main()