import random
num = random.randint(1,100)

tries = 0

while True:
    guessed = int(input("guess your number: "))
    tries += 1

    if guessed == num:
        print(f"congratulation you guess the right number in {tries} trials")
        break
    elif guessed>num:
        print("you need to go lower")

    elif guessed < num:
        print("you need to go higher")
