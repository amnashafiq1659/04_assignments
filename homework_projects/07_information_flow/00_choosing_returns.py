# Define the age at which a person is considered an adult
adult_age: int = 18


# Function to determine if a person is an adult or not
def is_adult(age: int):

    # Check if the person's age is greater than or equal to the adult age
    if age >= adult_age:

        # Return a message indicating that the person is an adult
        return "This person is an adult. ✅"

    # Return a message indicating that the person is not an adult
    return "This person is not an adult. ❌"


# Main function to test the is_adult function
def main():

    # Get the person's age from the user and call the is_adult function to determine if they are an adult or not
    age: int = int(input("How old is this person? "))
    print(is_adult(age))


if __name__ == "__main__":
    main()
