"""
CP1404 Practical 5
Emails
Estimate: 15 minutes
Actual: 24 minutes
"""


def main():
    """Stores users emails(keys) and names(values) into a dictionary"""
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        name = get_name_from_email(email)
        answer = input(f"Is your name {name}: ").upper()
        if answer != "Y" and answer != "":
            name = input("Name: ")
        email_to_name[email] = name
        email = input("Email: ")
    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def get_name_from_email(email):
    """Determine possible name from email"""
    prefix = email.split('@')[0]
    parts = prefix.split('.')
    name = " ".join(parts).title()
    return name


main()
