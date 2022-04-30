A,B,C = map(int, input().split())
n = 1
while True:
    cost = A + B*n
    benefit  = C * n
    n += 1

    if  benefit >= cost:
        print(n)
        break