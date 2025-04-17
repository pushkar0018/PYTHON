def rock_paper_scissors():
    valid_choices = ["rock", "paper", "scissors"]

    while True:
        # Get user input
        player_1 = input("Player 1, enter rock/paper/scissors: ").strip().lower()
        player_2 = input("Player 2, enter rock/paper/scissors: ").strip().lower()

        # Validate input
        if player_1 not in valid_choices or player_2 not in valid_choices:
            print("Invalid input. Please enter rock, paper, or scissors.")
            continue  # Restart the loop

        # Check for a tie
        if player_1 == player_2:
            print("It's a tie! Try again.")
            continue  # Restart the loop

        # Determine winner using a dictionary
        winner_map = {
            "rock": "scissors",
            "scissors": "paper",
            "paper": "rock"
        }

        if winner_map[player_1] == player_2:
            print("Player 1 wins!")
        else:
            print("Player 2 wins!")

        # Ask if they want to play again
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != "yes":
            break  # Exit the loop

rock_paper_scissors()

