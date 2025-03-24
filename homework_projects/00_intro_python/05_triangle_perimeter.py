# This function prompts the user to enter the lengths of the sides of a triangle and then calculates the perimeter of the triangle.
def calculate_triangle_perimeter():

    # Prompt the user to enter the lengths of the sides of a triangle.
    side1: float = float(input("Enter the length of side 1?: "))
    side2: float = float(input("Enter the length of side 2?: "))
    side3: float = float(input("Enter the length of side 3?: "))

    # Calculate the perimeter of the triangle.
    perimeter: float = side1 + side2 + side3

    # Print the perimeter of the triangle.
    print(f"The perimeter of the triangle is {perimeter}")


if __name__ == "__main__":
    calculate_triangle_perimeter()
