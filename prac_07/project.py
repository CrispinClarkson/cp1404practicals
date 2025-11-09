class Project:
    """Project class to store Project data."""
    def __init__(self, name, start_date, priority, cost_estimation, completion_percentage):
        """Initialise the Project object."""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimation = cost_estimation
        self.completion_percentage = completion_percentage

    def __str__(self):
        """Return a string representation of the Project."""
        date_format = self.start_date.strftime('%d/%m/%Y')
        return (f"{self.name}, start: {self.start_date.strftime('%d/%m/%y')}, priority {self.priority}, "
                f"estimate: ${self.cost_estimation:.2f}, completion: {self.completion_percentage}%")

    def is_complete(self):
        """Return true if the project is complete, otherwise return false."""
        return self.completion_percentage == 100

    def __lt__(self, other):
        """Compare projects by priority."""
        return self.priority < other.priority

    def __gt__(self, other):
        """Compare projects by priority."""
        return self.start_date > other.start_date
