# Define the number of days in a year
days_per_year: int = 365

# Define the number of hours in a day
hours_per_day: int = 24

# Define the number of minutes in an hour
minutes_per_hour: int = 60

# Define the number of seconds in a minute
seconds_per_minute: int = 60


# Function to calculate the number of seconds in a year
def seconds_in_year():

    # Calculate the number of seconds in a year
    seconds_per_year: int = (
        days_per_year * hours_per_day * minutes_per_hour * seconds_per_minute
    )

    # Print the result
    print(f"There are {seconds_per_year} seconds in a year!")


if __name__ == "__main__":
    seconds_in_year()
