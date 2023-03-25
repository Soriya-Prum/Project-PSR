""""Guessing game"""
from random import randint
while True:
    Bot = randint(1, 10)
    player = int(input("Can you guess the number from 0-10 correctly?   "))
    print("Bot = ", Bot)
    if player == Bot :
        print("Congratulation!")
    elif player > Bot:
        print("Too high, try again!")  
    else:
        print("Too low, try again!")
    replay = input("Do you want to play it again? n/N = exit:  ")
    if replay == "N" or replay == "n":
        break