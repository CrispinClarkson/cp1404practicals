from prac_07.guitar import Guitar

FILENAME = "guitars.csv"


def main():
    """Guitar program"""
    guitars = load_guitars(FILENAME)
    print("My Guitars:")

    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        print(f"{name} ({year}) : ${cost:.2f} added.")
        guitars.append(Guitar(name, year, cost))
        name = input("Name: ")

    guitars.sort()
    display_guitars(guitars)
    save_guitars(guitars, FILENAME)


def load_guitars(filename):
    """Load the guitars from a CSV file."""
    guitars = []
    with open(filename, "r") as input_file:
        for line in input_file:
            parts = line.strip().split(',')
            guitars.append(Guitar(parts[0], int(parts[1]), float(parts[2])))
        # print(guitars)
    return guitars


def save_guitars(guitars, filename):
    """Save Guitars to a CSV file."""
    with open(filename, "w") as output_file:
        for guitar in guitars:
            print(f"{guitar.name},{guitar.year},{guitar.cost:.2f}", file=output_file)


def display_guitars(guitars):
    """Display Guitars."""
    for guitar in guitars:
        print(f"Guitar: {guitar.name:<30}, Year: {guitar.year:<6}, Cost: ${guitar.cost}")


main()
