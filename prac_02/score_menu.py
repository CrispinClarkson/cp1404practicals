def main():
    score = get_valid_score()
    print("Menu: ")
    choice = input("> ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            print_result(score)
        elif choice == "S":
            show_stars(score)
        else:
            print("Invalid choice")
        print("Menu: ")
        choice = input("> ").upper()
    print("Farewell")


def determine_result(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def print_result(score):
    print(f"Score: {score} is {determine_result(score)}")


def get_valid_score():
    score = int(input("Enter Score: "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = int(input("Enter Score: "))
    return score


def show_stars(score):
    for i in range(score):
        print("*", end=" ")
    print()


main()
