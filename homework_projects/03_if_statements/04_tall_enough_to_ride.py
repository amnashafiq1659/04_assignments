# Define minimum height to ride
minimum_height: int = 50


# Function to check if the user is tall enough to ride
def main():

    # Prompt the user to enter their height
    height = float(input("How tall are you?"))

    # Check if the user is tall enough to ride and print the appropriate message
    if height >= minimum_height:
        print("You are tall enough to ride!")
    else:
        print("You are not tall enough to ride, but maybe next year!")


if __name__ == "__main__":
    main()
