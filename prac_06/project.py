# import datetime


class Project:

    def __init__(self, name="", start_date="", priority=0, estimate=0.0, completion=0):
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.estimate = estimate
        self.completion = completion

    def __str__(self):
        return f"{self.name}, start: {self.start_date}, priority {self.priority}, estimate: ${self.estimate}, " \
               f"completion: {self.completion}% "

    def is_complete(self):
        return self.completion == 100

# if __name__ == "__main__":
