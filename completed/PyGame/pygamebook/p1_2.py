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

#틱택토게임: 값 갱신해야 하므로 튜플이 아니라 리스트 이용

data = [[0,0,1],[1,2,2],[0,0,0]]

#리스트, 튜플 다루는 데 펴리한 함수

len([1,2,3,4])

a = [1,2,3]
b = a
a[2] = 9
##b[2]도 9임. 생성이 아니라 참조이기 때문에

a = [1,2,3]
b = a.copy()
a[2] = 9
#b[2]는 9가 아니라 3

#in

greets = ("morning", "afternnoon", "night")
"noon" in greets
##false return

greet = ("a","b","c")
greet.index("a") ##0 return. 값 찾을 수 없으면 오류 리턴

#sort, sorted
#sorted:인수로 주어진 리스트나 튜플을 정렬해 복사본 반환

#sort:리스트 정렬. 반환값 음슴
fruit = ["banana", "apple", "peach"]
sorted(fruit) ##정렬한 복사본 반환
fruit.sort() ##원본 정렬만함

#%연산자
val =1
name =4
print("val=%d, name=%s"%(val, name))

#format
"1={}, 2={}".format("one","two")
"3={1},4={0}".format("four","three")

'''

#행이 길어질경우 \ 삽입하여 줄바꿈
is_game_over = head in self.bodies or \
    head[0]<0 or head[0]==W or \
    head[1]==0

#삼항연산자
x=10 if a>10 else 0
x=(a>0)? 10:20
'''





