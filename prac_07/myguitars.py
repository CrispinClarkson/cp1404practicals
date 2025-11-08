from prac_07.guitar import Guitar


def main():
    """Guitar program"""
    guitars = []
    input_file = open("guitars.csv", "r")
    input_file.readline()
    for line in input_file:
        parts = line.strip().split(',')
        guitars.append(Guitar(parts[0], parts[1], parts[2]))
    # print(guitars)
    guitars.sort()

    for guitar in guitars:
        print(f"Guitar: {guitar.name:<30}, Year: {guitar.year:<6}, Cost: ${guitar.cost}")


main()

