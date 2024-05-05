import random

user_wins = 0
computer_wins = 0

while True:
    user_input = input("Type Rock/Paper/Scissor or Q to quit.").lower()
    if user_input == 'q':
        quit()

    if user_input in ["rock", "paper", "scissor"]:
        continue

    random_number = random.randint(0, 2)

print("Goodbye!")
