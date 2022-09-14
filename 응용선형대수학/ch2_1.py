#2X3 영행렬, 모든 성분이 1인 2x2행렬, 모든 성분이 3인 3x2행렬, 2x2 단위행렬을 만들어 출력하는 프로그램을 작성하라
import numpy as np

a = np.zeros((2,3))
print("a=",a)

b = np.ones((2,2))
print("b=",b)

c = np.full((3,2),3)
print("c=",c)

d = np.eye(2)
print("d=",d)