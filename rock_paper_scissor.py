import random
# In this game, you choose "rock," "paper," or "scissors," and the computer also makes a choice. The game then determines the winner based on the rules: rock beats scissors, scissors beat paper, and paper beats rock. If both you and the computer choose the same option it's a tie. You can play as many rounds as you like. 
def play_rock_paper_scissors():
    choices = ["rock", "paper", "scissors"]

    print("Welcome to Rock, Paper, Scissors!")
    while True:
        # Computer's choice
        computer_choice = random.choice(choices)

        # Player's choice
        player_choice = input("Enter your choice (rock, paper, scissors): ").lower()

        if player_choice not in choices:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            continue

        print(f"Computer chose: {computer_choice}")
        print(f"You chose: {player_choice}")

        if player_choice == computer_choice:
            print("It's a tie!")
        elif (
            (player_choice == "rock" and computer_choice == "scissors") or
            (player_choice == "scissors" and computer_choice == "paper") or
            (player_choice == "paper" and computer_choice == "rock")
        ):
            print("You win!")
        else:
            print("Computer wins!")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break

if __name__ == "__main__":
    play_rock_paper_scissors()
