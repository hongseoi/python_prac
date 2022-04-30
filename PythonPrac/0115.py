#for문으로 곱셈표 출력하기
number = [1,2,3,4,5,6,7,8,9]
for i in number:
    print(2*i)

for i in range(1,10):
    print(i)

#for문으로 19단표 출력
for i in range(1,20):
    for j in range(1,20):
        print(f'{i}x{j}={i*j}')

#문자열 포매팅으로 print 함수 사용하기: print('%d를 포함한 출력 내용'%(%d에 넣을 숫자))
print('나는 어제 사과 %d개를 먹었습니다.'%2)

#부가세 출력 프로그램 만들기: lambda 함수
y = lambda x : 3*x
y(12)
add =lambda a,b : a-b
add(2,3)
littleprince = '여섯살에 보았던 동화책에는 코끼리를 삼킨 보아뱀 그림이 그려져 있었다. 그 책에는 이렇게 쓰여 있었다.'
short = lambda x : x[:10]
short(littleprince)

#def문으로 함수 만들기
def add(a,b):
    return a+b
    
