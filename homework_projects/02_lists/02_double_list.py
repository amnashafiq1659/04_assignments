# Function to double the list
def double_list():

    # List of numbers to double
    numbers: list[int] = [1, 7, 3, 9, 5]

    # Double the list
    for i, number in enumerate(numbers):

        # Double the number
        numbers[i] = number * 2

    # Print the list
    print(numbers)


if __name__ == "__main__":

    double_list()
