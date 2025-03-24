# Write a program that reads numbers from the user and stores them in a list. The program should then display the count of each number in the list. Use a dictionary to solve this problem.
def get_user_numbers():

    # Get user input and store it in a list
    user_numbers = []

    # Get user input until user enters an empty string
    while True:
        user_input = input("Enter a number: ")
        if user_input == "":
            break
        number = int(user_input)
        user_numbers.append(number)
    return user_numbers


# Count the number of times each number appears in the list
def count_numbers(num_lst):

    # Create a dictionary to store the count of each number
    num_dict = {}

    # Count the number of times each number appears in the list and store it in the dictionary
    for num in num_lst:
        if num not in num_dict:
            num_dict[num] = 1
        else:
            num_dict[num] += 1
    return num_dict


# Print the count of each number in the dictionary
def print_count(num_dict):

    # Print the count of each number in the dictionary
    for num in num_dict:
        print(f"{num} appears {num_dict[num]} times.")


def main():
    # Get user input and count the number of times each number appears in the list
    user_numbers = get_user_numbers()
    num_dict = count_numbers(user_numbers)
    print_count(num_dict)


if __name__ == "__main__":
    main()
