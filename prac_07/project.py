class Project:
    """..."""
    def __init__(self, name, start_date, priority, cost_estimation, completion_percentage):
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimation = cost_estimation
        self.completion_percentage = completion_percentage

    def __str__(self):
        pass

    def __repr__(self):
        pass

    def is_complete(self):
        pass

    def __lt__(self, other):
        pass
