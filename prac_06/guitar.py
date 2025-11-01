"""
Guitar
Estimate: 18 minutes
Actual:
"""


class Guitar:
    """Guitar class to store guitar details."""

    def __init__(self, name="", year=0, cost=0):
        """Initialise a Guitar object."""
        self.name = name
        self.year = year
        self.cost = cost
