import random
import sys

while True:
    name = input("name:(if you want to exit hit the enter key")
    if name == "":
        sys.exit()

    question = input("What can  I do for you? ")
    print("Dr. "+name, "you asked me a question on \"", question, ".")
    print("Let me roll the dice of your destiny...")

    answers = random.randint(1,8)

    if answers == 1:
        print("Yes, certainly")
    elif answers == 2:
        print("The prospect seems to be good.")
    elif answers == 3:
        print("You can trust me")
    elif answers == 4:
        print("well, it seems like no.")
    elif answers == 5:
        print("That's write, without a single doubt.")
    elif answers == 6:
        print("Yes, you certainly made a right decision.")
    elif answers == 7:
        print("My answer is No.")
    else:
        print("Please ask me again later.")