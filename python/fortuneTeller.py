import random
import time
from colorama import Fore, init

init(autoreset=True)

fortunes = [
    "You will find a hidden treasure behind your couch today",
    "A major breakthrough is coming in your coding journey. Bug-free days ahead!",
    "A delicious surprise involving melted cheese is in your near future.",
    "You will display immense courage today by closing 57 open browser tabs.",
    "An alien spaceship will pass by, but they'll skip abducting you because you're too cool.",
    "Your next cup of coffee or tea will grant you temporary superpowers. Use them wisely.",
]

name = input("Enter your name to look into the future: ").strip()

if name:
    fortune = random.choice(fortunes)
    print(f"\n🔮 {Fore.YELLOW}Shaking the mystical emoji crystal ball for {name}...")
    time.sleep(1.5)
    print("\n" + f"{Fore.MAGENTA}=" * 50)
    print(f"{Fore.GREEN}✨ {name}'s Fortune ✨")
    print(f"{Fore.WHITE}{fortune}")
    print(f"{Fore.MAGENTA}=" * 50 + "\n")
else:
    print(f"{Fore.RED}The spirits require a name! Try running the program again.")
