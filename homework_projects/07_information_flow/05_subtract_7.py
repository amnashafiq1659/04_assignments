# Function for subtracting 7 from a number
def subtract_seven(num):

    # Subtract 7 from the given number and return the result
    num = num - 7
    return num


# Main function to take a number from the user and print the result after subtracting 7
def main():

    # Take a number from the user and store it in the variable num
    num = int(input("Enter a number: "))

    # Call the subtract_seven function with the given number and store the result in the variable result
    result = subtract_seven(num)

    # Print the result after subtracting 7 from the given number
    print(f"The result after subtracting 7 is: {result}")


if __name__ == "__main__":
    main()
