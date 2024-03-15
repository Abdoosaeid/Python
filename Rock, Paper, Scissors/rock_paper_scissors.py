import random

user_score = 0
computer_score = 0

option=["rock","paper","scissors"]

while True:
    player = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if player =="q":
        break

    if player not in option:
        continue

    random_number = random.randint(0,2)

    computer_pick=option[random_number]

    print("computer picked",computer_pick,".")

    if player == "rock" and computer_pick == "scissors":
        print("You won!")
        user_score += 1

    elif player == "paper" and computer_pick == "rock":
        print("You won!")
        user_score += 1

    elif player == "scissors" and computer_pick == "paper":
        print("You won!")
        user_score +=1

    elif player == computer_pick:
        print("Draw!")

    else :
        print("You lost!")
        computer_score +=1

print("You won",user_score,"times.")
print("The computer won",computer_score,"times.")
print("Goodbye!")



