# Function that returns a greeting message
def main():
    # Prompt the user to enter their name and store it in the name variable.
    name: str = input("What's your name: ")

    # Call the greet function with the user's name as an argument and store the result in the greeting variable.
    print(greet(name))


# Function that prints a greeting message with the user's name.
def greet(name):

    # Return the greeting message with the user's name.
    return f"Hello, {name}!"


if __name__ == "__main__":
    main()
