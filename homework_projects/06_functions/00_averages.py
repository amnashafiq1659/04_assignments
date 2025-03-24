# function that takes two numbers as arguments and returns the average of the two numbers.
def average(num1: float, num2: float):

    # Calculate the sum of the two numbers and divide by 2 to get the average.
    sum = num1 + num2
    return sum / 2


# function that calls the average function with two numbers, then calls the average function with the two averages.
def main():

    # Call the average function with two numbers.
    average1 = average(2, 4)
    average2 = average(10, 20)
    final_average = average(average1, average2)

    # Print the averages.
    print(f"Average 1: {average1}")
    print(f"Average 2: {average2}")
    print(f"final average: {final_average}")


if __name__ == "__main__":
    main()
