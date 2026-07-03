import random
from colorama import Fore, init

init(autoreset=True)

print(f"{Fore.CYAN}I'm thinking of a number between 1 and 100.")
print(f"{Fore.YELLOW}You have 7 attempts to guess it right. Good luck!\n")

secret_number = random.randint(1, 100)
attempts = 0
max_attempts = 7
won = False

while attempts < max_attempts:
    remaining_attempts = max_attempts - attempts
    print(f"{Fore.YELLOW}Attempts remaining: {remaining_attempts}")

    try:
        guess = int(input(f"{Fore.CYAN}Take a guess:"))
    except ValueError:
        print(f"{Fore.RED}Invalid input! Please enter a whole number.\n")
        continue

    attempts += 1

    if guess < secret_number:
        print(f"{Fore.RED}Too low! Try a higher number.\n")
    elif guess > secret_number:
        print(f"{Fore.RED}Too high! Try a lower number.\n")
    else:
        print(f"{Fore.GREEN}CONGRATULATIONS! You guessed it in {attempts} attempts!")
        won = True
        break  # Game over, exit loop

if not won:
    print(
        f"{Fore.RED}Game over! You ran out of guesses. The secret number was {secret_number}."
    )
