# Dictionary of fruits and their stock
inventory = {
    "apple": 30,
    "banana": 48,
    "orange": 120,
    "grape": 200,
    "kiwi": 80,
    "mango": 56,
    "pear": 78,
    "peach": 92,
    "cherry": 150,
    "watermelon": 40,
}


# Function to check the stock of a given fruit
def num_in_stock(fruit: str):

    # Convert the fruit name to lowercase for case insensitivity
    fruit = fruit.strip().lower()

    # Check if the fruit is in the inventory and return its stock
    return inventory.get(fruit, 0)


# Main function to test the num_in_stock function
def main():
    # Get user input for the fruit name and check its stock
    fruit = input("Enter a fruit: ")
    stock = num_in_stock(fruit)

    # Print the stock message based on the result
    if stock == 0:
        print(f"The fruit {fruit} is not in stock.")
    else:
        print(f"The fruit {fruit} is in stock. Here is how many it is: {stock}")


if __name__ == "__main__":
    main()
