# function that takes a number as an argument and returns the double of that number.
def double(num: int):

    # Multiply the number by 2 and return the result.
    return num * 2


# Main function that takes a number from the user and prints the double of that number.
def main():

    try:
        # Take a number from the user.
        num = int(input("Enter a number: "))

    except ValueError:
        print("Please enter a valid number")

    # Call the double function with the user's number and print the result.
    double_num = double(num)
    print(f"The double of {num} is {double_num}")


if __name__ == "__main__":
    main()
