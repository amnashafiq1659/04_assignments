# This function prompts the user to enter their favorite animal and then prints a message that the favorite animal is also the user's favorite.
def ask_favorite_animal():

    # Prompt the user to enter their favorite animal.
    favorite_animal: str = input("What's your favorite animal? ")

    # Print a message that the favorite animal is also the user's favorite.
    print(f"My favorite animal is also {favorite_animal}!")


if __name__ == "__main__":
    ask_favorite_animal()
