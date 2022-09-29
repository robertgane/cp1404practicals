def main():
    length = 8
    password = get_password(length)
    print_password(password)


def print_password(password):
    print("*" * len(password))


def get_password(length):
    password = input("Password: ")
    while len(password) < length:
        print("Password not long enough")
        password = input("Password: ")
    return password


main()
