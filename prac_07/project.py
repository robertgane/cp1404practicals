class Project:
    """Load from file and manage projects."""

    def __init__(self, name="", start_date="", priority=0, estimate=0.0, completion=0):
        """Initialize project attributes."""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.estimate = estimate
        self.completion = completion

    def __repr__(self):
        """Represent projects."""
        return f"{self.name}, start: {self.start_date}, priority {self.priority}, estimate: ${self.estimate}, " \
               f"completion: {self.completion}% "

    def is_complete(self):
        """Determine if project is complete."""
        return self.completion == 100

# if __name__ == "__main__":
