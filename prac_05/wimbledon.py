"""
Wimbledon
Estimate: 30 minutes
Actual: 51 minutes
"""

FILENAME = "wimbledon.csv"
INDEX_COUNTRY = 1
INDEX_CHAMPION = 2


def main():
    """Read data from csv file, print champion name and country."""
    records = load_records(FILENAME)
    champion_to_count, countries = process_records(records)
    display_results(champion_to_count, countries)


def load_records(filename):
    """Load records from csv file."""
    records = []
    with open(filename, "r", encoding="utf-8-sig") as input_file:
        input_file.readline()
        for line in input_file:
            parts = line.strip().split(",")
            records.append(parts)
        return records


def process_records(records):
    """Create dictionary of champion name and country."""
    champion_to_count = {}
    countries = set()
    for record in records:
        countries.add(record[INDEX_COUNTRY])
        try:
            champion_to_count[record[INDEX_CHAMPION]] += 1
        except KeyError:
            champion_to_count[record[INDEX_CHAMPION]] = 1
    return champion_to_count, countries


def display_results(champion_to_count, countries):
    """Print champion name and country."""
    print("Wimbledon Champions: ")
    for name, count in champion_to_count.items():
        print(f"{name} {count}")
    print(f"These {len(countries)} countries have won Wimbledon: ")
    print(", ".join(sorted(countries)))


main()
