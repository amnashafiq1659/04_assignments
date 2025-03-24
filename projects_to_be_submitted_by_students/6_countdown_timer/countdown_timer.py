# Import the time module
import time


# Function that takes an integer input from the user and starts a countdown timer for that many seconds.
def countdown_timer(seconds):

    # Print the starting message and start the countdown timer.
    print("⏰ Timer started!")
    while seconds:
        print(seconds)
        time.sleep(1)
        seconds -= 1

    # Print the completion message when the countdown timer is completed.
    print("⏰ Timer completed!")


# Take the input from the user and call the countdown_timer function.
seconds = int(input("Enter the time in seconds: "))

if __name__ == "__main__":
    countdown_timer(seconds)
