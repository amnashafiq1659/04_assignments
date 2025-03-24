# Define the different voting ages for the different countries
peturksbouipo_age: int = 16
stanlau_age: int = 25
mayengua_age: int = 48


# Define a function that will take the user's age and determine if they can vote in the different countries
def voting_status():

    # Prompt the user to enter their age
    user_age = int(input("How old are you:"))

    # Check if the user can vote in Peturksbouipo
    if user_age >= peturksbouipo_age:
        print(
            f"You can vote in Peturksbouipo where the voting age is {peturksbouipo_age}."
        )
    else:
        print(
            f"You cannot vote in Peturksbouipo where the voting age is {peturksbouipo_age}."
        )

    # Check if the user can vote in Stanlau
    if user_age >= stanlau_age:
        print(f"You can vote in Stanlau where the voting age is {stanlau_age}.")
    else:
        print(f"You cannot vote in Stanlau where the voting age is {stanlau_age}.")

    # Check if the user can vote in Mayengua
    if user_age >= mayengua_age:
        print(f"You can vote in Mayengua where the voting age is {mayengua_age}.")
    else:
        print(f"You cannot vote in Mayengua where the voting age is {mayengua_age}.")


if __name__ == "__main__":
    voting_status()
