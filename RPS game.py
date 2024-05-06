import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissor"]


while True:
    user_input = input("Type Rock/Paper/Scissor or Q to quit : ").lower()
    if user_input == 'q':
        break

    if user_input not in ["rock", "paper", "scissor"]:
        continue

    random_number = random.randint(0, 2)
    # rock :0 ,paper :1 ,scisssor :2

    computer_pick = options[random_number]
    print("Computer picked", computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissor":
        print("You won!")
        user_wins += 1
        continue

    elif user_input == "paper" and computer_pick == "rock":
        print("You won!")
        user_wins += 1

    elif user_input == "scissor" and computer_pick == "paper":
        print("You won!")
        user_wins += 1
    elif user_input == computer_pick:
        print("Draw! Try again")
    else:
        print("You lost!")
        computer_wins += 1

print("You won", user_wins, "times..")
print("Computer won", computer_wins, "times..")

print("Goodbye!")
