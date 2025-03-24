# Functions for checking if a number is odd or even
def main():
    # Test the is_odd function with numbers from 0 to 9
    for num in range(10):
        if is_odd(num):
            print(f"{num} is odd")
        else:
            print(f"{num} is even")


# Function to print the number of odd numbers in the given range
def is_odd(value: int):
    # Check if the number is divisible by 2 (remainder is 1)
    remainder = value % 2
    return remainder == 1


if __name__ == "__main__":
    main()
