import random
import tkinter as tk

# List of possible color names and their corresponding RGB values
colors = {
    "red": "#FF0000",
    "green": "#00FF00",
    "blue": "#0000FF",
    "yellow": "#FFFF00",
    "magenta": "#FF00FF",
    "cyan": "#00FFFF",
    
}

# Function to select a random color
def select_random_color():
    return random.choice(list(colors.keys()))

# Function to start a new round
# Function to start a new round
def new_round():
    # Get a random color
    random_color_name = select_random_color()
    random_color = colors[random_color_name]
    
    # Display the color inside a rectangle
    canvas.itemconfig(rectangle, fill=random_color)
    
    # Clear the input field
    input_entry.delete(0, tk.END)
    
    # Set the focus to the input field
    input_entry.focus()

    # Update the current color
    label.config(text=f"Type the color: {random_color_name}", fg=random_color)



# Function to check the player's input
def check_input():
    player_color = input_entry.get().strip().lower()
    random_color_name = label.cget("text").split(": ")[1]  # Corrected this line

    if player_color == random_color_name:
        result_label.config(text="Correct! You guessed the color correctly.", fg="green")
    else:
        result_label.config(text=f"Wrong! The correct color was {random_color_name}.", fg="red")

    # Start a new round
    new_round()


# Create the main window
window = tk.Tk()
window.title("Color Prediction Game")

# Create a canvas to display the color
canvas = tk.Canvas(window, width=200, height=100)
canvas.pack()

# Create a rectangle to display the color
rectangle = canvas.create_rectangle(10, 10, 190, 90, fill="white")

# Create a label to instruct the player
label = tk.Label(window, text="Type the color:", font=("Arial", 12))
label.pack()

# Create an entry field for the player's input
input_entry = tk.Entry(window, font=("Arial", 12))
input_entry.pack()

# Create a button to submit the player's input
submit_button = tk.Button(window, text="Submit", command=check_input)
submit_button.pack()

# Create a label to display the result
result_label = tk.Label(window, text="", font=("Arial", 12))
result_label.pack()

# Start the first round
new_round()

# Start the main loop
window.mainloop()
