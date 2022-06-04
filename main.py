# Rock, Paper, cissors Game
import random


#moves for the player
moves = ['rock', 'paper', 'scissors']

while True:
    computer = random.choice(moves)
    player = input("rock, paper or scissors? (or end the game)").lower()
    if player == "end the game":
        print("The game has ended.")
        break

    if player == computer:
        print("Tie!")
    elif player == 'rock':
        if computer == 'paper':
            print("You Lose!", computer, "beats", player)

        else:
            print("You Win!", player, "beats", computer)
            player_score += 1
    elif player == "paper":
        if computer == "scissors":
            print("You Lose!", computer, "beats", player)

        else:
            print("You win!", player, "beats", computer)

    elif player == "scissors":
        if computer == "rock":
            print("You Lose!", computer, "beats", player)

        else:
            print("You win!", player, "beats", computer)

    else:
        print("check your spelling")



