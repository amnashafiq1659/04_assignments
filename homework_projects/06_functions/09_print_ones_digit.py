# function that takes an integer as an argument and prints the ones digit of the integer.
def print_ones_digit(num):

    # calculate the ones digit by taking the remainder of the number divided by 10.
    ones_digit = num % 10

    # print the ones digit.
    print(f"The ones digit of {num} is {ones_digit}.")


# main function to test the print_ones_digit function.
def main():

    # get the number from the user.
    num = int(input("Enter a number: "))

    # call the print_ones_digit function.
    print_ones_digit(num)


if __name__ == "__main__":
    main()
