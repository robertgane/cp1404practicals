length = 8
password = input("Password: ")
while len(password) < length:
    print("Password not long enough")
    password = input("Password: ")
print("*" * len(password))
