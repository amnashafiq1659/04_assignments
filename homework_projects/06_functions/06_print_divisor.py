# function that prints the divisors of a number
def print_divisor(num: int):

    # print the number itself as a divisor
    print(f"Divisors of {num} are:")

    # iterate through all numbers from 1 to the given number
    for n in range(1, num + 1):

        # if the number is divisible by n, print n
        if num % n == 0:
            print(n)


# main function
def main():

    # take input from the user and print the divisors of the given number
    num = int(input("Enter a number: "))
    print_divisor(num)


if __name__ == "__main__":
    main()
