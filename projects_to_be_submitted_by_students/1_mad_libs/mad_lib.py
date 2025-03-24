# Import the random module to generate random stories
import random


# Function to generate mad lib story
def mad_lib():

    # Print a welcome message
    print("🎉Welcome to the Mad Lib Generator!")

    # Prompt the user to enter a name, place, animal, verb, adverb, and adjective
    while True:
        name = input("Enter a name: ")
        place = input("Enter a place: ")
        animal = input("Enter an animal: ")
        verb = input("Enter a verb: ")
        adverb = input("Enter an adverb: ")
        adjective = input("Enter an adjective: ")

        # List of stories to choose from
        stories = [
            f"One day, {name} was in {place} when a {adjective} {animal} bit them. Suddenly, they could {verb} at the speed of light! ‘I must use my powers to {verb} evil!’ {name} declared. But first, they had to finish their {adjective} homework.",
            f"At {place}, {name} decided to prank their {adjective} teacher. They put a {adjective} {animal} inside the teacher’s desk. But when the teacher opened it, the {animal} jumped out and started to {verb}! The whole class laughed until the principal walked in and {verb} at {name}!",
            f"At {place}, {name} found a {adjective} hat. When they put it on, a {animal} appeared and started to {verb} {adverb}. ‘This is the best day ever!’ {name} shouted.",
            f"Inside {place}, {name} picked up a {adjective} book. Suddenly, a {animal} jumped out and began to {verb} {adverb}. ‘This is the weirdest library ever!’ {name} gasped.",
            f"While in {place}, {name} saw a {adjective} spaceship land. A tiny {animal} stepped out and started to {verb} {adverb}. ‘Well, that’s something you don’t see every day!’ {name} whispered.",
            f"While at {place}, {name} saw a {adjective} {animal} trying to {verb} {adverb}. It tripped and fell, then stood up like nothing happened. ‘Smooth move!’ {name} laughed.",
        ]

        # Randomly select a story from the list
        selected_story = random.choice(stories)

        # Replace the placeholders in the story with the user's input
        print("\n🎭 Here is your Mad Lib story:")

        # Print the story with the user's input
        print(selected_story)

        # Ask the user if they want to play again
        play_again = input("\n Do you want to play again? (yes/no): ")

        # If the user does not want to play again, print a goodbye message and break out of the loop
        if play_again.lower() != "yes":
            print("\n👋 Goodbye! Thanks for playing!")
            break


if __name__ == "__main__":
    mad_lib()
