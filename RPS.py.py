""""Rock Paper Scissors"""
from random import randint
print("Rock Paper Scissors Game")
while True:
    
    random_num = randint(0, 3)

    if random_num == 0:
        Bot = "rock"
    elif random_num == 1:
        Bot = "paper"
    else:
        Bot = "scissors"

    player = input("player : ")
    if player == Bot:
        print("Bot: ",Bot)
        print("Tie")

    elif player == "rock":
        print("Bot: ",Bot)
        if Bot == "paper":
            print("You Lose")
        else:
            print("You Win")

    elif player == "scissor":
        print("Bot: ",Bot)
        if Bot == "rock":
            print("You Lose")
        else:
            print("You Win")

    elif player == "paper":
        print("Bot: ",Bot)
        if Bot == "scissors":
             print("You win")
        else:
            print("You Lose")
            
    else:
        print("Your move is not valid!")
    replay = input("Do you want to play it again? n/N = exit:  ")
    if replay == "N" or replay == "n":
        break