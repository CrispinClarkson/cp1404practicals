"""
Guitar Test
Estimate: 14 minutes
Actual: 16 minutes
"""
from prac_06.guitar import Guitar

CURRENT_YEAR = 2025


def run_tests():
    """Test for guitar class."""
    name = "Gibson L-5 CES"
    year = 1922
    cost = 16035.40

    guitar = Guitar(name, year, cost)
    different_guitar = Guitar("Fender Boxer Series ST557", 1985, 1350.00)

    print(f"{guitar.name} get_age() - Expected 103. Got {guitar.get_age()}")
    print(f"{different_guitar.name} get_age() - Expected 40. Got {different_guitar.get_age()}")

    print(f"{guitar.name} is_vintage() - Expected True. Got {guitar.is_vintage()}")
    print(f"{different_guitar.name} is_vintage() - Expected False. Got {different_guitar.is_vintage()}")


run_tests()
