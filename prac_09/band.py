from prac_09.musician import Musician


class Band:
    """Band class represents a group of musicians."""
    def __init__(self, name):
        """Initialise a Band instance."""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return a string representation of the band."""
        return f"{self.name} ({",".join([str(musician) for musician in self.musicians])}"

    def add(self, musician):
        """Add musician to the band."""
        self.musicians.append(musician)

    def play(self):
        """Return which musician is currently playing."""
        for musician in self.musicians:
            print(musician.play())
            