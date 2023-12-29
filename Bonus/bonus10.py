#logical issues
try:
    width = float(input("Enter rectangle width: "))
    length = float(input("Enter rectangle length: "))

    if width == length:
        exit("That is a square.")  # This is to ensure user does not enter values of square. This is a logic error and needs to be handled in code.

    area = width * length

    print(area)
except ValueError:
    print("Please enter a number.")