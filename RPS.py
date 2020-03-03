from random import randint


t = ["Rock", "Paper", "Scissors"]


computer = t[randint(0,2)]


player = False

while player == False:

    player = input("Rock, Paper, Scissors?")
    if player == computer:
        print("Tie, try again!")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose!", computer, "beats", player)
        else:
            print("You win!", player, "beats", computer)
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!", computer, "beats", player)
        else:
            print("You win!", player, "beats", computer)
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose...", computer, "beats", player)
        else:
            print("You win!", player, "beats", computer)
    else:
        print("I do not recognize this input, please try again!")
        player = False
    computer = t[randint(0,2)]
