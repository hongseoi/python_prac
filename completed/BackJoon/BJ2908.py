'''
1트

a,b = map(int, input().split())
n = max(a,b)

for i in len(n):
    print(n[2-i])

int형은 len(), 슬라이싱 사용 불가능
for문에는 반복할 수 있는 객체, 리스트나 스트링만 가능
'''
#2트

a,b = input().split()

a = a[::-1]
b = b[::-1]

if int(a) > int(b):
    print(a)
else:
    print(b)
