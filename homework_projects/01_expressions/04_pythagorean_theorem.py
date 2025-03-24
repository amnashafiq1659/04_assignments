# Import the math library
import math


# Function to calculate the hypotenuse of a right triangle
def pythagorean_theorem():

    # Prompt the user to enter the length of AB
    ab: float = float(input("Enter the length of AB: "))

    # Prompt the user to enter the length of AC
    ac: float = float(input("Enter the length of AC: "))

    # Calculate the hypotenuse of the right triangle
    bc: float = math.sqrt(ab**2 + ac**2)

    # Print the hypotenuse of the right triangle
    print(f"The length of BC (the hypotenuse) is: {bc}")


if __name__ == "__main__":
    pythagorean_theorem()
