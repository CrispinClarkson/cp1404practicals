"""
Estimated Time: 2:30 hours
Actual Time:
"""

MENU = ("- (L)oad projects \n- (S)ave projects \n- (D)isplay projects \n- (F)ilter projects by date"
        "\n- (A)dd new projects \n- (U)pdate project \n- (Q)uit")


def main():
    """..."""
    print("Welcome to Pythonic Project Management")
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            load_projects()
        elif choice == "S":
            save_projects()
        elif choice == "D":
            display_projects()
        elif choice == "F":
            filter_projects()
        elif choice == "A":
            add_projects()
        elif choice == "U":
            update_projects()
        else:
            print("Invalid menu choice")
        print(MENU)
        choice = input(">>> ").upper()
    quit_projects()


def load_projects():
    pass


def save_projects():
    pass


def display_projects():
    pass


def filter_projects():
    pass


def add_projects():
    pass


def update_projects():
    pass


def quit_projects():
    pass


main()
