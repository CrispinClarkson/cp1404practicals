LENGTH = 10
password = input("Enter password: ")
while len(password) < LENGTH:
    print("Password is invalid, try again")
    password = input("Enter password: ")
print("*" * len(password))