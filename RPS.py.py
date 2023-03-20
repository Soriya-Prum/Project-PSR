from random import randint

computer = randint(0, 3)

if computer == 0: 
    Bot = "rock"
elif computer == 1:
    Bot = "paper"
else:
    Bot = "scissors"

player = input("Player: ")

if player == Bot:
    print("Bot = ", Bot)
    print("Tie")
elif player == "paper":
    if Bot == "scissors":
        print("Bot = ", Bot)
        print("Bot win!")
    else:
        print("Bot = ", Bot)
        print("Player win!")
elif player == "rock":
    if Bot == "scissors":
        print("Bot = ", Bot)
        print("Player win!")
    else:
        print("Bot = ", Bot)
        print("Bot win!")
elif player == "scissor":
    if Bot == "paper":
        print("Bot = ", Bot)
        print("Player win!")
    else:
        print("Bot = ", Bot)
        print("Bot win!")
else:
    print("Please enter the valid choice!")