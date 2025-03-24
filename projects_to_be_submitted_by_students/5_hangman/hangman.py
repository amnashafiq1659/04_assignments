# Import random module to generate random words
import random

# Import string module to generate all uppercase letters
import string

# List of words to choose from
words = ["sunshine", "rainbow", "adventure", "galaxy", "treasure", "happiness"]


# Function to get a valid word from the list
def get_valid_word(words):

    # Randomly select a word from the list
    word = random.choice(words).upper()

    # Check if the word contains invalid characters and select a new word if it does
    while "-" in word or " " in word:
        word = random.choice(words).upper()
    return word


# Function to play the hangman game
def hangman():

    # Create a welcome message
    print("\n🎮 Welcome to Hangman Game!")

    # Get a valid word from the list
    word = get_valid_word(words)

    # Initialize the variables
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    # Initialize the number of lives as 6
    lives = 6

    # Loop to play the game
    while len(word_letters) > 0 and lives > 0:
        # Display the current state of the word with guessed letters filled in or dashes
        print(
            f"\nYou have {lives} lives left. You have used: {' '.join(used_letters) if used_letters else 'None'}"
        )

        word_list = [letter if letter in used_letters else "-" for letter in word]
        print(f"Current word: {' '.join(word_list)}")

        # Get the user's input
        user_letter = input("Guess a letter: ").upper()

        # Check if the user's input is valid and update the game state accordingly
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)

            # Check if the user's letter is in the word
            if user_letter in word_letters:
                word_letters.remove(user_letter)

            else:
                lives -= 1
                print("❌ Wrong guess! That letter is not in the word.")

        elif user_letter in used_letters:
            print("🔄 You already used that letter. Try again.")

        else:
            print("⚠ Invalid character. Please enter a valid letter.")

    # Display the final state of the game
    if lives == 0:
        print(f"\n💀 You lost! The word was: {word}")

    else:
        print(f"\n🎉 Congratulations! You guessed the word {word} correctly!")


if __name__ == "__main__":
    hangman()
