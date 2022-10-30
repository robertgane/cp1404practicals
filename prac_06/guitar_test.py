from prac_06.guitar import Guitar

gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
another = Guitar("Another Guitar", 2013, 8453.60)
print(f"{gibson.name} get_age() - Expected 100. Got {gibson.get_age()}")
print(f"{another.name} get_age() - Expected 9. Got {another.get_age()}")
print(f"{gibson.name} is_vintage() - Expected True. Got {gibson.is_vintage()}")
print(f"{another.name} is_vintage() - Expected False. Got {another.is_vintage()}")
