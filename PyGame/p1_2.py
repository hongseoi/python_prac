# 몫과 나머지 한번에 구하기
from functools import total_ordering


print(divmod(11,4))
print(float(True))

#bool 형으로 바꾸기: 0, 0.0, 빈 문자열은 False, 나머지는 True
print(bool(''))
print(bool("hello"))

# 튜플: 생성 후 값 수정 불가능
subject = (10,20,30,40)
total = 0
for i in range(4):
    total += subject[i]
print(total)

# 리스트
weekday = ['월','화','수', '목', '금','토']
weekday.append('일')
weekday.insert(2,'이요일')
print(weekday)
del weekday[2]
print(weekday)
weekday.pop(1)
print(weekday)

#딕셔너리
score = {
    'math':78,
    "english":95,
    "chemistry":43
}

score["math"]

score["chemistry"] =44

#리스트의 리스트
animals = ("horse", "lion", "elephant")
score = (34,33,22)
data=(animals, score)