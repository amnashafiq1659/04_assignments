# This function calculates the ages of five friends and prints them.
def calculate_ages():

    # Anton is 21 years old.
    Anton: int = 21

    # Beth is 6 years older than Anton.
    Beth: int = 6 + Anton

    # Chen is 20 years older than Beth.
    Chen: int = 20 + Beth

    # Drew is as old as Chen's age plus Anton's age.
    Drew: int = Chen + Anton

    # Ethan is the same age as Chen.
    Ethan: int = Chen

    # Print the ages of the five friends.
    print(f"Anton is {Anton} years old.")
    print(f"Beth is {Beth} years old.")
    print(f"Chen is {Chen} years old.")
    print(f"Drew is {Drew} years old.")
    print(f"Ethan is {Ethan} years old.")


if __name__ == "__main__":
    calculate_ages()
