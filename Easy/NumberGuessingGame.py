import random

def number_guessing_game():
    secret_number = random.randint(1, 100)
    max_attempts = 10
    attempts = 0
    
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print(f"You have {max_attempts} attempts to guess it.\n")
    
    while attempts < max_attempts:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid integer.")
            continue
        
        attempts += 1
        
        if guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too high!")
        else:
            print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts!")
            return
        
        remaining = max_attempts - attempts
        if remaining > 0:
            print(f"{remaining} attempts left.\n")
        else:
            print(f"Game over! The secret number was {secret_number}.")
    

if __name__ == "__main__":
    number_guessing_game()