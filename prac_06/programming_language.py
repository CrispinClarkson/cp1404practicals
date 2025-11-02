class ProgrammingLanguage:
    """Programming language class to determine language status'."""

    def __init__(self, name, typing, reflection, year):
        """Initialise a programming language instance. """
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Return True if this programming language is dynamic."""
        return self.typing == "Dynamic"

    def __str__(self):
        """Return string of car showing its name, fuel and odometer readings."""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First Appeared in {self.year}"
