

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    print("Let's drive!")
    print(MENU)
    choice = input(">>> ").lower()
    while choice != "q":
        if choice == "d":
            drive_taxis()
        elif choice == "c":
            choose_taxi()
        else:
            print("Invalid option.")
        choice = input(">>> ").lower()


def drive_taxis():
    pass


def choose_taxi():



if __name__ == '__main__':
    main()
