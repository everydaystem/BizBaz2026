from colorama import Fore, init

init(autoreset=True)

languages_voted = ["python", "javascript", "python", "rust", "python", "go"]
target_language = "python"

count = 0

for lang in languages_voted:
    if lang == target_language:
        count = +1  # Bug

print(f"{Fore.CYAN}Searching for: {target_language}")
print(f"{Fore.GREEN}Total count found: {count}")
