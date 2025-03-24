# Import the random module to generate random choice
import random

# Function to play the game
def play_game():
    
    # List of choices
    choice = ["rock", "paper", "scissors"]

    # Print the instructions
    print("\n🎮 Welcome to Rock, Paper, Scissors Game!")

    # While loop to keep the game running
    while True:
        user_choice = input("\nChoose rock, paper or scissors: ").lower()

        # Check if the user's choice is valid and continue to the next iteration if not
        if user_choice not in choice:
            print("⚠️ Invalid choice. Please choose rock, paper or scissors.")
            continue

        # Generate a random choice for the computer and print it
        computer_choice = random.choice(choice)

        print(f"\n🖥️ Computer chose: {computer_choice}.")

        # Print the result of the game
        print(determine_winner(user_choice, computer_choice))


# Function to determine the winner based on the user's and computer's choices
def determine_winner(user_choice, computer_choice):

    # Check for a tie or determine the winner based on the user's and computer's choices.
    if user_choice == computer_choice:
        return "🤝 It's a tie!"

        # Check for the winning conditions
    elif user_choice == "rock":
        if computer_choice == "scissors":
            return "🎉 You win!"
        else:
            return "😞 You lose!"

    elif user_choice == "paper":
        if computer_choice == "rock":
            return "🎉 You win!"
        else:
            return "😞 You lose!"

    elif user_choice == "scissors":
        if computer_choice == "paper":
            return "🎉 You win!"
        else:
            return "😞 You lose!"


if __name__ == "__main__":
    play_game()
