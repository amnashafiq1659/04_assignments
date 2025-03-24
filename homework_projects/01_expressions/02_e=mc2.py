# Speed of light in meters per second
C: int = 299792458


# Function to calculate the energy of a mass
def calculate_energy():

    # Prompt the user to enter the mass in kilograms
    mass_in_kg: float = float(input("Enter the mass in kilograms: "))

    # Calculate the energy in joules
    energy_in_joules: float = mass_in_kg * (C**2)

    # Print the formula
    print("e = m * C^2...")

    # Print the mass in kilograms
    print(f"m = {mass_in_kg} kg")

    # Print the speed of light in meters per second
    print(f"C = {C} m/s")

    # Print the energy in joules
    print(f"{energy_in_joules} joules of energy!")


if __name__ == "__main__":
    calculate_energy()
