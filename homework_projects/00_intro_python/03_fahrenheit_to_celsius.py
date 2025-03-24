# This function prompts the user to enter a temperature in Fahrenheit and then converts it to Celsius.
def convert_fahrenheit_to_celsius():

    # Prompt the user to enter a temperature in Fahrenheit.
    degrees_fahrenheit: float = float(input("Enter the temperature in Fahrenheit: "))

    # Convert the temperature to Celsius.
    degrees_celsius: float = (degrees_fahrenheit - 32.00) * (5.0 / 9.0)

    # Print the temperature in Celsius.
    print(f"Temperature: {degrees_fahrenheit}°F = {degrees_celsius}°C")


if __name__ == "__main__":
    convert_fahrenheit_to_celsius()
