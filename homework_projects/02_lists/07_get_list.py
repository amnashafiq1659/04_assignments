#Function to print list
def get_list():

    #Make an empty list to store values
    lst = []

    #Prompt the user to enter a value
    val = input("Enter a value:")

    while val:
        lst.append(val)
        val = input("Enter a value:")

    #Print the list
    print("Here's the list:",lst)

if __name__ == '__main__':
    get_list()    
