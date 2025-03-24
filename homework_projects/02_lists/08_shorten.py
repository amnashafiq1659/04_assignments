# define a maximum length of the list
max_length: int = 3


# define a function to shorten the list
def shorten(lst):

    # while the length of the list is greater than the maximum length
    while len(lst) > max_length:

        # remove the last element of the list
        last_element = lst.pop()

        # print the last element
        print(f"Removed: {last_element}")
        
    print(f"final list {lst}")    


# define a function to get the list
def get_list():

    # initialize an empty list to store the elements of the list
    lst = []

    # prompt the user to enter an element of the list
    element = input("Please enter an element of the list or press enter to stop:")

    # while the user does not press enter
    while element != "":

        # append the element to the list
        lst.append(element)

        # prompt the user to enter an element of the list
        element = input("Please enter an element of the list or press enter to stop:")

    return lst


# define a function to display the list
def display_list():

    # print the list
    lst = get_list()

    # shorten the list
    shorten(lst)


if __name__ == "__main__":
    display_list()
