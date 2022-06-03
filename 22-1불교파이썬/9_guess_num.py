import random

tries = 0
guess = 0

answer = random.randint(1,100)

print("Guess the number between 1 and 100")

while guess != answer:
    guess = int(input("Enter the number:"))
    tries += 1

    if guess < answer:
        print("Low!")
    elif guess > answer:
        print("Hight!")

if guess == answer:
    print("congratulations, the number of attempts=", tries)
else:
    print("The answer is ", number)
