import random

class NumberGuessingGame:
    def __init__(self, difficulty="medium"):
        self.difficulty = difficulty
        self.set_target_number_range()
        self.target_number = random.randint(self.min_value, self.max_value)
        self.score = 0
        self.rounds = 0
        self.max_attempts = self.set_max_attempts()
        self.best_score = float('inf')  # To track the best score ever
        
    def set_target_number_range(self):
        if self.difficulty == "easy":
            self.min_value, self.max_value = 1, 10
        elif self.difficulty == "hard":
            self.min_value, self.max_value = 1, 50
        else:
            self.min_value, self.max_value = 1, 20
    
    def set_max_attempts(self):
        if self.difficulty == "easy":
            return 5
        elif self.difficulty == "hard":
            return 3
        else:
            return 4
    
    def welcome_message(self):
        print(f"Welcome to the Number Guessing Game! Difficulty: {self.difficulty.capitalize()}")
        print(f"Guess a number between {self.min_value} and {self.max_value}.")
        print(f"You have {self.max_attempts} attempts per round. Enter 'Q' or 'q' to quit.")

    def get_user_input(self):
        while True:
            user_input = input("Enter your guess: ")
            if user_input.lower() == 'q':
                return user_input
            try:
                guess = int(user_input)
                if self.min_value <= guess <= self.max_value:
                    return guess
                else:
                    print(f"Please enter a number between {self.min_value} and {self.max_value}.")
            except ValueError:
                print(f"Invalid input. Please enter a number between {self.min_value} and {self.max_value} or 'Q' to quit.")

    def check_guess(self, guess, attempts_left):
        if guess == self.target_number:
            print("Congratulations! You've guessed the correct number.")
            self.score += 1
            self.rounds += 1
            if self.score < self.best_score:
                self.best_score = self.score
            print(f"Your current score is: {self.score}")
            print(f"Rounds played: {self.rounds}")
            print(f"Best score: {self.best_score}")
            self.target_number = random.randint(self.min_value, self.max_value)  # Reset target number for next round
            return True
        else:
            if attempts_left > 1:
                if guess < self.target_number:
                    print("Your guess is too low. Try again!")
                elif guess > self.target_number:
                    print("Your guess is too high. Try again!")
            else:
                print("Sorry, you've used all your attempts. The correct number was:", self.target_number)
                self.target_number = random.randint(self.min_value, self.max_value)  # Reset target number for next round
            return False

    def play(self):
        self.welcome_message()
        while True:
            attempts_left = self.max_attempts
            while attempts_left > 0:
                guess = self.get_user_input()
                if guess == 'q':
                    print("Thank you for playing! Your final score is:", self.score)
                    print(f"Rounds played: {self.rounds}, Best score: {self.best_score}")
                    return
                attempts_left -= 1
                if self.check_guess(guess, attempts_left):
                    break

    @staticmethod
    def get_valid_difficulty():
        while True:
            difficulty = input("Choose difficulty (easy, medium, hard): ").lower()
            if difficulty in ['easy', 'medium', 'hard']:
                return difficulty
            else:
                print("Invalid input! Please choose from 'easy', 'medium', or 'hard'.")

if __name__ == "__main__":
    # Get valid difficulty input from the user
    difficulty = NumberGuessingGame.get_valid_difficulty()
    game = NumberGuessingGame(difficulty)
    game.play()
