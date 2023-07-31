'''
가우스 조단 소거법을 수행하는 gause()라는 함수를 정의하고 이 함수를 이용해서 다음 연립 선형 방정식의 해를 구하라.
p82 참조
'''

from turtle import shape
import numpy as np

def gause(A){
    (n,m) = A.shape
    
    for i in range(0,min(n.m)):
        


}

A = np.array([[2.,2.,4.,18.],
            [1.,3.,2.,13.],
            [3.,1.,3.,14.]])


print("A=",A)

x = gause(A)
