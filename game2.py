import tkinter as tk
import random

# List of words for the game
word_list = ["python", "java", "programming", "computer", "hangman", "javascript", "developer"]

# Function to select a random word from the list
def select_random_word():
    return random.choice(word_list)

# Function to scramble a word
def scramble_word(word):
    word_chars = list(word)
    random.shuffle(word_chars)
    return ''.join(word_chars)

# Function to start a new game
def new_game():
    global word_to_guess, scrambled_word, attempts_left
    word_to_guess = select_random_word()
    scrambled_word = scramble_word(word_to_guess)
    attempts_left = 3

    word_label.config(text="Unscramble the word: " + scrambled_word)
    attempts_label.config(text="Attempts left: " + str(attempts_left))
    guess_entry.delete(0, tk.END)

# Function to check the guess
def check_guess():
    global attempts_left
    guess = guess_entry.get().lower()
    
    if guess == word_to_guess:
        result_label.config(text="Congratulations! You guessed the word correctly.")
    else:
        attempts_left -= 1
        if attempts_left == 0:
            result_label.config(text=f"Game over. The word was: {word_to_guess}")
        else:
            result_label.config(text="Incorrect guess. Try again.")
            attempts_label.config(text="Attempts left: " + str(attempts_left))
    
    guess_entry.delete(0, tk.END)

# Create the main window
window = tk.Tk()
window.title("Word Unscramble Game")

# Create labels and entry field
word_label = tk.Label(window, text="", font=("Arial", 14))
word_label.pack()

attempts_label = tk.Label(window, text="", font=("Arial", 12))
attempts_label.pack()

guess_label = tk.Label(window, text="Your guess:", font=("Arial", 12))
guess_label.pack()
guess_entry = tk.Entry(window, font=("Arial", 12))
guess_entry.pack()

# Create a button to submit the guess
submit_button = tk.Button(window, text="Submit Guess", command=check_guess, font=("Arial", 12))
submit_button.pack()

# Create a button to start a new game
new_game_button = tk.Button(window, text="New Game", command=new_game, font=("Arial", 12))
new_game_button.pack()

# Create a label for game results
result_label = tk.Label(window, text="", font=("Arial", 12))
result_label.pack()

# Start a new game
new_game()

# Start the game
window.mainloop()
