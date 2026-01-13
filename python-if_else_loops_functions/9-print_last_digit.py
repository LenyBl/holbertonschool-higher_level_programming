def print_last_digit(number):
    """Prints the last digit of a number.

    Args:
        number (int): The number to extract the last digit from.
    Returns:
        int: The last digit of the number.
    """
    if number < 0:
        number = -number
    last_digit = abs(number) % 10
    print("{}".format(last_digit), end="")
    return last_digit
