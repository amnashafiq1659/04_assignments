# Functions for printing a message multiple times
def print_multiple(message: str, times: int):

    # Print the message multiple times
    for i in range(times):
        print(message)


# Main function to get user input and call the print_multiple function
def main():
    # Get user input for the message and the number of times to print it
    message = input("Please enter a message: ")
    times = int(input("Please enter the number of times to print the message: "))
    print_multiple(message, times)


if __name__ == "__main__":
    main()
