# 다음의 행렬, 벡터들의 크기를 출력하는 프로그램을 작성하라
'''

A =[[1,2,3]]         v=[1]          w=[1 2 3]              B=[1,2,3]
    [4,5,6]            [2]                                   [4,5,6]
    [7,8,9]            [3]

'''
#hint : numpy의 array를 이용해 행렬, 벡터 생성하고 shape로 크기 출력하기

import numpy as np

A = np.array([[1,2,3],[4,5,6],[7,8,9]])
v = np.array([[1],[2],[3]])
w = np.array([1,2,3])
B = np.array([[1,2,3],[4,5,6]])

print("A=", A, A.shape)
print("v=",v, v.shape)
print("w=",w, w.shape)
print("B=",B,B.shape)