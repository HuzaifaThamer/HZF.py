# ══════════════════════════════════════════
# 🐍 HZF.py — 30 Python Projects in 30 days
# 🎮 Day 01/30 — Number Guessing Game
# ══════════════════════════════════════════

import random

num= random.randint(1,100)

attempts= 7

RED= "\033[31m"
GREEN= "\033[32m"
BLUE= "\033[34m"
RESET= "\033[0m"

while attempts > 0:
    try:
        guessing= int(input("Guess the number: "))

        if guessing == num:
            print(f"{BLUE}You guessed right!!")
            break

        elif guessing > num:
            print(f"{RED}Lower{RESET}")
            attempts= attempts-1
            print(f"Attempts left: {attempts}")
            continue

        elif guessing < num:
            print(f"{GREEN}Higher{RESET}")
            attempts= attempts-1
            print(f"Attempts left: {attempts}")
            continue

    except ValueError:
        print(f"{RED}Invalid input{RESET}")

if attempts == 0:
    print(f"Game over, the correct number is{RESET}{BLUE} ({num})!")













