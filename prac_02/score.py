"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

import random


# TODO: Fix this!

def main():
    score = float(input("Enter score: "))
    result = determine_result(score)
    print(result)
    random_score = random.randint(1, 101)
    random_result = determine_result(random_score)
    print(random_result)


def determine_result(score):
    if score < 0:
        return "Invalid score"
    elif score > 100:
        return "Invalid score"
    elif score < 50:
        return "Bad"
    elif score < 90:
        return "Passable"
    else:
        return "Excellent"


main()
