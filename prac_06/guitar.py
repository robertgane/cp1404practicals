"""
CP1404/CP5632 Practical - Guitar program.
Estimate = 10 mins
Actual = 4 mins
"""

CURRENT_YEAR = 2022
VINTAGE_AGE = 50


class Guitar:

    def __init__(self, name="", year=0, cost=0):
        """Initialise a Guitar instance"""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost:,}"

    def get_age(self):
        """Get age of Guitar"""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Determine if Guitar is vintage"""
        return self.get_age() >= VINTAGE_AGE
