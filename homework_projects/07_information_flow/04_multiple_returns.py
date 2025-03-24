# Function to collect user information
def get_user_info():

    # Prompt the user to enter their information and store the values in variables.
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    email = input("Enter your email address: ")

    # Return the collected information.
    return first_name, last_name, email


# Function to print the collected user information.
def print_user_info():

    # Get the user information using the get_user_info function.
    first_name, last_name, email = get_user_info()

    # Print the collected information.
    print(f"\nReceived the following user data:")
    print(f"First Name: {first_name}")
    print(f"Last Name: {last_name}")
    print(f"Email: {email}")


if __name__ == "__main__":
    print_user_info()
