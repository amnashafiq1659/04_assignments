# Function to get the last element of the list
def get_last_element(lst):
    print(lst[-1])


# Function to get the list
def get_lst():
    # Initialize the list
    lst = []

    # Get the first element of the list
    element: str = input("Enter an element of the list:")

    # Check if the element is empty
    while not element:
        element = input("Enter at least one element of the list:")

    # Append the first element to the list
    lst.append(element)

    # Get the other elements of the list
    while True:

        # Get the next element of the list
        element = input("Enter another element of the list:")

        # Append the element to the list
        if element:
            lst.append(element)
        else:
            break
    return lst


# Function to get the first element of the list
def main():

    # Get the list
    lst = get_lst()

    # Get the first element of the list
    get_last_element(lst)


if __name__ == "__main__":
    main()
