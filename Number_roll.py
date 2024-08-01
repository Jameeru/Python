import random

class NumberGuessingGame:
    def __init__(self, lower_bound=1, upper_bound=100):
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound
        self.target_number = None
        self.attempts = 0
        self.difficulty = 'medium'

    def set_difficulty(self):
        difficulty_levels = {
            'easy': 10,
            'medium': 7,
            'hard': 5
        }
        while True:
            print("\nSelect Difficulty Level:")
            for level in difficulty_levels:
                print(f"- {level.capitalize()}")
            choice = input("Enter difficulty level: ").lower()
            if choice in difficulty_levels:
                self.difficulty = choice
                self.max_attempts = difficulty_levels[choice]
                print(f"Difficulty set to {choice.capitalize()}. You have {self.max_attempts} attempts.")
                break
            else:
                print("Invalid choice. Please choose again.")

    def start_new_game(self):
        self.target_number = random.randint(self.lower_bound, self.upper_bound)
        self.attempts = 0
        print(f"\nGuess the number between {self.lower_bound} and {self.upper_bound}.")

    def guess_number(self, guess):
        self.attempts += 1
        if guess < self.target_number:
            print("Too low!")
        elif guess > self.target_number:
            print("Too high!")
        else:
            print(f"Congratulations! You've guessed the number {self.target_number} in {self.attempts} attempts.")
            return True
        return False

    def play(self):
        self.set_difficulty()
        self.start_new_game()
        while self.attempts < self.max_attempts:
            try:
                guess = int(input(f"Attempt {self.attempts + 1}/{self.max_attempts}. Enter your guess: "))
                if self.guess_number(guess):
                    break
            except ValueError:
                print("Invalid input. Please enter a number.")
        else:
            print(f"Sorry, you've used all your attempts. The correct number was {self.target_number}.")

def main():
    game = NumberGuessingGame()

    while True:
        game.play()
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thank you for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()
