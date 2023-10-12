import tkinter as tk
import random

# Function to create an empty tic-tac-toe board
def create_board():
    return [[" " for _ in range(3)] for _ in range(3)]

# Function to check if a player has won
def check_win(board, player):
    # Check rows
    for row in board:
        if all(mark == player for mark in row):
            return True

    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

# Function to check if the board is full
def is_full(board):
    return all(mark == "X" or mark == "O" for row in board for mark in row)

# Function to make a move
def make_move(row, col):
    global player
    if board[row][col] == " " and not game_over:
        board[row][col] = player
        buttons[row][col].config(text=player)
        if player == "X":
            player = "O"
        else:
            player = "X"

        # Check if a player has won
        if check_win(board, "X"):
            announce_winner("You win!")
        elif check_win(board, "O"):
            announce_winner("Computer wins!")
        # Check for a tie
        elif is_full(board):
            announce_winner("It's a tie!")

        # If it's the computer's turn, make its move
        if player == "O" and not game_over:
            row, col = computer_move(board)
            make_move(row, col)

# Function to announce the winner
def announce_winner(message):
    global game_over
    game_over = True
    winner_label.config(text=message)
#How do I undo the most recent local commits in Git?
# Function to restart the game
def restart_game():
    global board, player, game_over
    board = create_board()
    player = "X"
    game_over = False
    winner_label.config(text="")
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(text=" ")

# Create the main tkinter window
root = tk.Tk()
root.title("Tic-Tac-Toe")

# Initialize the game variables
board = create_board()
player = "X"
game_over = False

# Create the buttons for the game board
buttons = [[None, None, None] for _ in range(3)]

for i in range(3):
    for j in range(3):
        buttons[i][j] = tk.Button(root, text=" ", font=("Helvetica", 20), width=6, height=2,
                                  command=lambda row=i, col=j: make_move(row, col))
        buttons[i][j].grid(row=i, column=j)

# Create a button to restart the game
restart_button = tk.Button(root, text="Restart", font=("Helvetica", 14), command=restart_game)
restart_button.grid(row=3, column=0, columnspan=3)

# Create a label to display the winner
winner_label = tk.Label(root, text="", font=("Helvetica", 16))
winner_label.grid(row=4, column=0, columnspan=3)

# Start the tkinter main loop
root.mainloop()
