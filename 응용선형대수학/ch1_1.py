# 정수의 개수를 입력받고 해당하는 개수만큼의 정수를 입력받아 합을 계산하는 함수 calc()를 작성하라

from itertools import count


def calc(num):
    sum = 0
    for i in range(0,num):
        sum += int(input())
    return sum

print("input the number >>")
count = int(input())
print(calc(count))

