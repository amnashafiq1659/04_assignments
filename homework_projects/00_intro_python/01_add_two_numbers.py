# This function prompts two integer inputs from the user and calculates their sum.
def add_two_numbers():

    # Prompt the user to enter the first number.
    num1: str = input("Enter the first number: ")

    # Read the input and convert it to an integer.
    num1: int = int(num1)

    # Prompt the user to enter the second number.
    num2: str = input("Enter the second number: ")

    # Read the input and convert it to an integer.
    num2: int = int(num2)

    # Calculate the sum of the two numbers.
    sum: int = num1 + num2

    # Print the total sum with an appropriate message.
    print(f"The total sum of the two numbers is {sum}.")


if __name__ == "__main__":
    add_two_numbers()
