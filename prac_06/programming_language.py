"""CP1404/CP5632 Practical - Programming language.
Estimate: 15 mins
Actual: 23 mins
"""


class ProgrammingLanguage:
    """Represent a Programming Language object."""

    def __init__(self, field, typing, reflection, year):
        """Represent a Programming Language object."""
        self.field = field
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        return f"{self.field}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"

    def is_dynamic(self):
        return self.typing == "Dynamic"
