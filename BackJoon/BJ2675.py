
T = int(input())

for i in range(T):
    R, s = input().split()
    text = ''

    for i in s:
        text += int(R)*i

    print(text)
