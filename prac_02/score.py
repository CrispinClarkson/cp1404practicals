"""
CP1404/CP5632 - Practical
Program to determine score status
"""

import random


def main():
    """Get user score and generate random score."""
    score = float(input("Enter score: "))
    result = determine_result(score)
    print(result)

    random_score = random.randint(0, 100)
    print(f"Random Score: {random_score} {determine_result(random_score)}")


def determine_result(score):
    """Determine result based on score."""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
