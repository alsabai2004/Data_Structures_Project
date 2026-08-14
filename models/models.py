def readInt():
    while True:
        try:
            return int(input("Enter integer value: "))
        except ValueError:
            print("Please enter a valid integer.")


def readFloat():
    while True:
        try:
            return float(input("Enter float value: "))
        except ValueError:
            print("Please enter a valid number.")


def read():
    return input("Enter string value: ")
