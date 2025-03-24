# Add three copies of the data to the end of the list
def add_three_copies(my_list, data):

    # Add the data to the end of the list three times
    for i in range(3):
        my_list.append(data)


# function to print the list before and after the function is called
def main():

    # Get the message from the user
    message = input("Enter a message to copy: ")

    # Create an empty list
    my_list = []

    # Print the list before the function is called
    print(f"List before: {my_list}")

    # Call the function to add three copies of the data to the end of the list
    add_three_copies(my_list, message)

    # Print the list after the function is called
    print(f"List after: {my_list}")


if __name__ == "__main__":
    main()
