# Define the sentence start
sentence_start: str = "A robot suddenly appeared and said,"


# Define the mad lib function
def mad_lib():

    # Prompt the user to enter an adjective
    adjective: str = input("Enter an adjective: ")

    # Prompt the user to enter a noun
    noun: str = input("Enter a noun: ")

    # Prompt the user to enter a verb
    verb: str = input("Enter a verb: ")

    # Print the mad lib
    print(f'{sentence_start} "I am a {adjective} {noun} and i love to {verb}!"')


if __name__ == "__main__":
    mad_lib()
