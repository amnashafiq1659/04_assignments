# function that asks the user for their name and returns it.
def get_name():
    # Prompt the user to enter their name.
    name = input("Enter your name: ")
    # Return the name.
    return name


# Main function that calls the get_name function and prints a greeting with the user's name.
def main():
    # Call the main function.
    name = get_name()
    # Print a greeting with the user's name.
    print(f"Hello, {name}!")


if __name__ == "__main__":
    main()
