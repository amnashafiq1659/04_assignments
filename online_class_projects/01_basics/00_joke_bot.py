# Prompt the user to enter something
prompt: str = "What do you want?"

# Define a joke for the joke_bot function
joke: str = (
    "Why did the frontend developer break up with the backend developer? There was too much API drama! 💔"
)

# Define a message for the joke_bot function if the user doesn't ask for a joke
sorry: str = "Sorry, I only tell jokes!"


# Define the joke_bot function
def joke_bot():

    # Get the user's input from the prompt
    user_input: str = input(prompt)

    # Check if the user asked for a joke and print the joke if so, otherwise print a sorry message
    if "joke" in user_input:
        print(joke)
    else:
        print(sorry)


if __name__ == "__main__":
    joke_bot()
