# function that takes a list of integers as a parameter and returns the number of even numbers in the list.
def count_even(lst):

    # Get the number of even numbers
    count = 0

    # Iterate through the list and increment the count if the number is even. 0 % 2 == 0 checks if a number is even. 1 % 2 == 0 checks if a number is odd. 0 % 2 != 0 checks if a number is odd. 0 % 2 == 0 is the same as 2 % 2 == 0. 1 % 2 != 0 is the same as 3 % 2
    for num in lst:
        if num % 2 == 0:
            count += 1
    return count


# Get a list of integers from the user
def get_list_of_ints():

    # Create an empty list to store the integers.
    lst = []

    # Get the integers from the user
    while True:
        user_input = input("Enter an integer or press enter to stop: ")

        # If the user presses enter, stop the loop
        if user_input == "":
            break

        # Try to convert the user input to an integer. If it fails, print an error message.
        try:
            lst.append(int(user_input))

        except ValueError:
            print("Invalid input. Please enter an integer.")

    return lst


# Call the main function to execute the program


def main():

    lst = get_list_of_ints()
    print(f"The number of even numbers in the list is {count_even(lst)}")


if __name__ == "__main__":
    main()
