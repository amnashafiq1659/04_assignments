# Function to make a sentence based on the part of speech of a word
def make_sentence(word: str, part_of_speech: int):
    # Check the part of speech and print the appropriate sentence.
    if part_of_speech == 0:
        print(f"I am excited to add this {word} to my vast collection of them!")
    elif part_of_speech == 1:
        print(f"It's so nice outside today it makes me want to {word}!")
    elif part_of_speech == 2:
        print(f"Looking out my window, the sky is big and {word}!")
    else:
        print("Invalid input. Please enter 0, 1, or 2.")


# Main function to get user input and call the make_sentence function
def main():

    # Get user input for the word and part of speech.
    word = input("Enter a noun, verb, or adjective: ")
    print("Is this a noun, verb, or adjective?")
    part_of_speech = int(
        input("Enter the part of speech (0: noun, 1: verb, 2: adjective): ")
    )

    # Call the make_sentence function with the user input.
    make_sentence(word, part_of_speech)


if __name__ == "__main__":
    main()
