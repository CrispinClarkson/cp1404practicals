CURRENT_YEAR = 2025
VINTAGE_AGE = 50


class Guitar:
    """Guitar class to store guitar details."""

    def __init__(self, name="", year=0, cost=0):
        """Initialise a Guitar object."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a string representation of the Guitar."""
        return f"{self.name} ({self.year}) : ${self.cost:.2f}"

    def get_age(self):
        """Return the age of the Guitar."""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Return True if the Guitar is vintage."""
        return self.get_age() >= VINTAGE_AGE

    def __lt__(self, other):
        """Return True if the Guitar is less than the other Guitar."""
        return self.year < other.year
