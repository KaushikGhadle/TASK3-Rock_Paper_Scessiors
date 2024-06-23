import random

def get_user_choice():
    """Get the user's choice and validate input."""
    choices = ['rock', 'paper', 'scissors']
    user_choice = input("Enter rock, paper, or scissors: ").lower()
    while user_choice not in choices:
        print("Invalid choice. Please try again.")
        user_choice = input("Enter rock, paper, or scissors: ").lower()
    return user_choice

def get_computer_choice():
    """Randomly select a choice for the computer."""
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    """Determine the winner based on the classic rules of the game."""
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "user"
    else:
        return "computer"

def play_game():
    """Main function to play the game."""
    print("####### WELCOME TO ROCK_PAPER_SCISSORS GAME #######")
    
    user_score = 0
    computer_score = 0
    ties = 0
    
    while True:
        print("\n" + "*"*40)
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"\nYou chose: {user_choice.capitalize()}")
        print(f"Computer chose: {computer_choice.capitalize()}")
        
        winner = determine_winner(user_choice, computer_choice)
        if winner == "user":
            print("Result: You win!")
            user_score += 1
        elif winner == "computer":
            print("Result: You lose!")
            computer_score += 1
        else:
            print("Result: It's a tie!")
            ties += 1
        
        print("\n" + "-"*40)
        print(f"Scores:\nYou: {user_score} | Computer: {computer_score} | Ties: {ties}")
        print("-"*40)
        
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("\nThanks for playing!")
            print("="*40)
            print(f"Final Scores:\nYou: {user_score} | Computer: {computer_score} | Ties: {ties}")
            print("="*40)
            break

# Start the game
if __name__ == "__main__":
    play_game()
