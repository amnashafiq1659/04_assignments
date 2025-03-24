# Conversion factor. There are 12 inches for 1 foot
inches_per_foot: int = 12


# Function to convert feet to inches
def convert_feet_to_inches():

    # Prompt the user to enter the number of feet
    feet: float = float(input("Enter the number of feet: "))

    # Convert the feet to inches
    inches: float = feet * inches_per_foot

    # Print the result
    print(f"That is {inches} inches!")


if __name__ == "__main__":
    convert_feet_to_inches()
