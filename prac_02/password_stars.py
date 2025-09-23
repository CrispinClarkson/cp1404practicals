LENGTH = 10


def main():
    """  """
    password = get_password()
    print_stars(password)


def print_stars(password):
    """ Print stars based on length of password"""
    print("*" * len(password))


def get_password():
    """ Get valid password  """
    password = input("Enter password: ")
    while len(password) < LENGTH:
        print("Password is invalid, try again")
        password = input("Enter password: ")
    return password


main()
