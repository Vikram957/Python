import random
cscore = 0
uscore = 0

while True:
    Score = print(f"your score is {uscore} and computer score is {cscore}")
    user = int(input("1 for stone , 2 for paper , 3 for scissors choose:"))
    comp = random.randint(1,3)

    if user == 1 and comp == 3:
        print("you won this round \n")
        uscore +=1

    elif user == 2 and comp == 1:
        print("you won this round \n")
        uscore +=1
        

    elif user == 3 and comp == 2:
        print("you won this round \n")
        uscore +=1
        

    elif user == comp:
        print("it was a draw round \n")
        

    else:
        print("computer won this round \n")
        cscore +=1

    if cscore == 5:
        print("computer won the game")
        break

    elif uscore == 5:
        print("you won the game")
        break
