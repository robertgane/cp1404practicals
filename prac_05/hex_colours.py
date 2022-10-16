"""
CP1404 Practical 5
Hexadecimal colour code program
"""

COLOUR_TO_CODE = {"absolute zero": "#0048ba", "acid green": "#b0bf1a", "aliceblue": "#f0f8ff",
                  "alizarin crimson": "#e32636", "amaranth": "#e52b50", "amber": "#ffbf00", "amethyst": "#9966cc",
                  "antiquewhite": "#faebd7", "antiquewhite1": "#ffefdb", "antiquewhite2": "#eedfcc"}

colour_name = input("Enter colour name: ").lower()
while colour_name != "":
    try:
        print(f"The colour code for {colour_name.title()} is {COLOUR_TO_CODE[colour_name]}")
    except KeyError:
        pass  # Left out invalid message as question does not ask for it
    colour_name = input("Enter colour name: ").lower()
