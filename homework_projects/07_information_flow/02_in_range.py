# Function returns a message indicating whether a number is in a given range.
def in_range(n, low, high):
    # Check if the number is in the given range and return a corresponding message.
    if n >= low and n <= high:
        return f"✅ {n} is in the range of {low} and {high}."
    return f"❌ {n} is NOT in the range of {low} and {high}."


# Main function to test the in_range function.
def main():
    # Get user input for the number, lower bound, and upper bound.
    n = int(input("Enter a number (n): "))
    low = int(input("Enter the lower bound (low): "))
    high = int(input("Enter the upper bound (high): "))

    # Call the in_range function and print the result.  # Example usage: in_range(15, 10, 20) -> "✅ 15 is in the range of 10 and 20."  # Example usage: in_range(25, 10, 20) -> "❌ 25 is NOT in the range of 10 and 20."  # Example usage: in_
    print(in_range(n, low, high))


if __name__ == "__main__":
    main()
