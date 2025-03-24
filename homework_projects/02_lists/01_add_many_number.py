# Function to add many numbers
def add_many_numbers(numbers) -> int:

    # Return the sum of all numbers in the list
    return sum(numbers)


# Function to print the sum of all numbers in the list
def main():

    # List of numbers to add
    numbers: list[int] = [6, 2, 8, 4, 10]

    # Sum of all numbers in the list
    sum_of_numbers: int = add_many_numbers(numbers)

    # Print the sum of all numbers in the list
    print(sum_of_numbers)


if __name__ == "__main__":
    main()
