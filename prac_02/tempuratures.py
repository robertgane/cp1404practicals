"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
print(MENU)
choice = input(">>> ").upper()


def calculate_fahrenheit(celsius_value):
    fahrenheit_value = celsius_value * 9.0 / 5 + 32
    return fahrenheit_value


def calculate_celsius(fahrenheit_value):
    celsius_value = 5 / 9 * (fahrenheit_value - 32)
    return celsius_value


while choice != "Q":
    if choice == "C":
        celsius = float(input("Celsius: "))
        fahrenheit = calculate_fahrenheit(celsius)
        print("Result: {:.2f} F".format(fahrenheit))
    elif choice == "F":
        fahrenheit = float(input("Fahrenheit: "))
        celsius = calculate_celsius(fahrenheit)
        print("Result: {:.2f} C".format(celsius))
    else:
        print("Invalid option")
    print(MENU)
    choice = input(">>> ").upper()
print("Thank you.")
