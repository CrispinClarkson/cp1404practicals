"""
Guitars
Estimate: 30 minutes
Actual: 27 minutes
"""
from prac_06.guitar import Guitar


def main():
    """Guitar program"""
    print("My guitars!")
    guitars = []
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        print(f"{name} ({year}) : ${cost:.2f} added.")
        guitars.append(Guitar(name, year, cost))
        name = input("Name: ")

    # guitars.append(Guitar("Fender Stratocaster", 2014, 765.4))
    # guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    # guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    print("These are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        vintage_mark = ""
        if guitar.is_vintage():
            vintage_mark = "(vintage)"
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth $ {guitar.cost:10,.2f} {vintage_mark}")


main()
