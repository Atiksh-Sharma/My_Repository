# Project Name - Guess the Number

import random

Target = random.randint(1, 100)

while True:
    userChoise = input("Guess the target or Quit(Q) : ")
    if(userChoise == "Q"):
        break 

    userChoise = int(userChoise)
    if(userChoise == Target):
        print("Success : Correct Guess!!")
        break
    elif(userChoise < Target):
        print("Your Guess number in small. Guess again")
    else:
        print("Your number is big, Guess again")

print("----GAME OVER-----")

