import random

num = int(input("Lottery number?(between0~99):"))

lotterynum = random.randint(0,99)
print("winning number is ", lotterynum)

ldigit1 = num//10
ldigit2= num%10

digit1 = lotterynum//10
digit2 = lotterynum%10

if digit1==ldigit1 and digit2 == ldigit2 :
    print("you get $1000!")

elif digit1==ldigit1 or digit2 == ldigit2:
    print("you get 500$")

else:
    print("no money")
