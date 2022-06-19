for index in range(5):
    print(index)

total = 0
for val in range(10):
    total += val

for val in range(3,7):
    print(val)

##처음은 0부터 포함 마지막은 포함하지 않는다.

#break: 조건문 하나 벗어남
#continue: 조건문 하나 앞으로 돌아감

for val in range(5):
    print(val)
    if val%2==0:
        continue
    print("===")
