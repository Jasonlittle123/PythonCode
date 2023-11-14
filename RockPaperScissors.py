import random

player1_wins = 0
player2_wins = 0

options = ["rock", "paper", "scissors"]

while True:
    player1_input = input("Type Rock/Paper/Scissor or Q to quit: ").lower()
    if player1_input == "q":
        break # you can use this quit()

    if player1_input not in options:
        continue

    random_number = random.randint(0, 2)
    #why i put (0, 2) because rock: 0, paper: 1, scissor: 2
    computer_pick = options[random_number]
    print("Computer picked", computer_pick + ".")

    if player1_input == "rock" and computer_pick == "scissors":
        print("You won")
        player1_wins += 1
        continue
    
    if player1_input == "paper" and computer_pick == "rock":
        print("You won")
        player1_wins += 1
        
    if player1_input == "scissors" and computer_pick == "paper":
        print("You won")
        player1_wins += 1
        
    else:
        print("You lost")
        player2_wins += 1

print("You Won", player1_wins, "Times")
print("The computer won", player2_wins, "Times")
print("GoodBye!")