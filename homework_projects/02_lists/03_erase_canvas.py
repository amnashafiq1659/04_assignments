import tkinter as tk

# Constants
canvas_width = 400
canvas_height = 400
cell_size = 40
eraser_size = 20


# Erase objects in the canvas
def erase_objects(event):
    # Get the mouse position
    mouse_x = event.x
    mouse_y = event.y

    # Calculate the bounding box of the eraser
    left_x = mouse_x
    top_y = mouse_y
    right_x = left_x + eraser_size
    bottom_y = top_y + eraser_size

    # Find all objects that overlap with the eraser
    overlapping_objects = canvas.find_overlapping(left_x, top_y, right_x, bottom_y)

    # Change the color of the overlapping objects to white
    for obj in overlapping_objects:
        canvas.itemconfig(obj, fill="white")


# Main function
def main():
    # Initialize the canvas
    global canvas
    # Create the main window
    root = tk.Tk()
    root.title("Erase Canvas")

    # Create the canvas
    canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg="white")
    canvas.pack()

    # Calculate the number of rows and columns in the canvas
    num_rows = canvas_width // cell_size
    num_cols = canvas_height // cell_size

    # Draw the cells in the canvas
    for row in range(num_rows):
        for col in range(num_cols):
            left_x = col * cell_size
            top_y = row * cell_size
            right_x = left_x + cell_size
            bottom_y = top_y + cell_size
            canvas.create_rectangle(
                left_x, top_y, right_x, bottom_y, fill="blue", outline="black"
            )

    # Draw the eraser
    eraser = canvas.create_rectangle(
        0, 0, eraser_size, eraser_size, fill="pink", outline="black"
    )

    # Move the eraser
    def move_eraser(event):
        canvas.coords(
            eraser, event.x, event.y, event.x + eraser_size, event.y + eraser_size
        )
        erase_objects(event)

    # Bind the eraser to the canvas
    canvas.bind("<Motion>", move_eraser)

    # Start the main loop
    root.mainloop()


if __name__ == "__main__":
    main()
