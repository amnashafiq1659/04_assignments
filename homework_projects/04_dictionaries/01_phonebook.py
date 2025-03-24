# Write a program that reads phone numbers from the user and stores them in a dictionary.
def read_phone_numbers():

    # Create an empty dictionary to store the phone numbers.
    phonebook = {}

    # The program will continue to prompt the user for name and phone number until the user enters an empty name.
    while True:
        name = input("Enter name: ")
        if name == "":
            break
        phone = input("Enter phone number: ")
        phonebook[name] = phone

    return phonebook


# Write a function that prints the phone numbers in the phonebook.
def print_phonebook(phonebook):

    # Iterate over the keys in the phonebook dictionary and print the name and phone number.
    for name in phonebook:
        print(f"{name}: {phonebook[name]}")


# Write a function that looks up phone numbers in the phonebook.
def lookup_numbers(phonebook):

    # Prompt the user for a name and lookup the phone number in the phonebook.  If the name is not found, print a message.  Otherwise, print the phone number.  The program will continue to prompt the user until the user enters an empty name.  The program will also handle case sensitivity.  For example, if the user enters "John" and "john", the program will consider them the same name.  The program will also handle cases where the user ent
    while True:
        name = input("Enter name to lookup: ")
        if name == "":
            break
        if name not in phonebook:
            print(f"{name} not found in phonebook")
        else:
            print(phonebook[name])


# Write the main function that calls the other functions.
def main():
    phonebook = read_phone_numbers()
    print_phonebook(phonebook)
    lookup_numbers(phonebook)


if __name__ == "__main__":
    main()
