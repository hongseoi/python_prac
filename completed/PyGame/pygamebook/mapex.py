'''
map(처리할 함수, 리스트나 튜플)
리스트나 튜플의 요소 전체에 대해 처리할 때 사용
'''

#map 이용해 두배로 만들기

def make_double(x):
    return x*2

list(map(make_double, [1,2,3]))
##[2,4,6] return

list(map(lambda x: x*2, [1,2,3]))
