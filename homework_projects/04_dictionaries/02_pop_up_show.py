# Function that asks the user how many of each fruit they want to buy.
def fruit_shop():

    # Dictionary of fruits and their prices
    fruits = {
        "apple": 15,
        "banana": 8,
        "orange": 10,
        "grape": 4,
        "kiwi": 5,
        "mango": 10,
        "pear": 7,
        "peach": 8,
        "cherry": 5,
        "watermelon": 50,
    }

    # Variable to store the total cost of the fruits bought
    total_cost = 0

    # Loop through the fruits dictionary
    for fruit_name in fruits:

        # Variable to store the price of the fruit
        price = fruits[fruit_name]

        # Ask the user how many of the fruit they want to buy
        fruit_bought = int(input(f"How many {fruit_name} do you want to buy? "))

        # Calculate the total cost of the fruits bought
        total_cost += price * fruit_bought

    # Print the total cost of the fruits bought
    print(f"The total cost of the fruits you bought is ${total_cost}")


if __name__ == "__main__":
    fruit_shop()
