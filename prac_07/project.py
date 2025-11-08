class Project:
    """..."""
    def __init__(self, name, start_date, priority, cost_estimation, completion_percentage):
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimation = cost_estimation
        self.completion_percentage = completion_percentage

    def __str__(self):
        return (f"{self.name}, start: {self.start_date}, priority {self.priority},"
                f"estimate: ${self.cost_estimation:.2f}, completion: {self.completion_percentage}%")

    def __repr__(self):
        return str(self)

    def is_complete(self):
        return self.completion_percentage == 100

    def __lt__(self, other):
        pass
