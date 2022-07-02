# 행렬 A와 벡터 V를 파이썬으로 정의하고 이를 출력하는 프로그램을 작성하라
'''
A=[1 2 3
   4 5 6
   7 8 9]

V = [1
     2
     3]
'''
#hint: numpy에서 array()로 행렬 벡터 생성하기

import numpy as np
A = np.array([[1,2,3],
            [4,5,6],
            [7,8,9]])

v = np.array([[1],[2],[3]])

print("A=",A)
print("v=",v)