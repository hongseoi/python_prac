#6009
from numpy import set_printoptions


a = input()
print(a)

#6010
n = int(input())
print(n)

#6011
f = float(input())
print(f)

#6020
a = input()
b = input()
print(a)
print(b)

#6013
a = input()
b = input()
print(b,a)

#6014
f = input()
print(f)
print(f)
print(f)

#6015
a, b = input().split()
print(a)
print(b)

#6016
n1, n2 = input().split()
print(n2, n1)

#6017
a, b = input().split(":")
print(a,b,sep=":")

#6019
y,m,d = input().split(".")
print(d,m,y, sep="-")

#6020
a,b = input().split("-")
print(a,b, sep="")

#6021
s = input()
for i in range(len(s)):
    print(s[i])

#6022
s = input()
print(s[0:2],s[2:4],s[4:],sep=" ")

#6023
h,m,s = input().split(":")
print(m)

#6024
w1,w2 = input().split()
print(w1+w2)

#6025
a,b = map(int,input().split())
print(a+b)