#26
a = float(input())
b = float(input())
print(a+b)

#27
a = int(input())
print('%x'%a)

#28
a = int(input())
print('%X'%a)

#29
a = input()
n = int(a, 16)
print('%o'%n)

#30
n = ord(input())
print(n)

#31
a = int(input())
print(chr(a))

#32
a = int(input())
print(-a)

#33
a = ord(input())
print(chr(a+1))

#34
a, b = map(int, input().split())
print(a-b)

#35
f1, f2 = map(float,input().split())
print(f1*f2)

#36
w, n = input().split()
print(w*int(n))

#37
n = int(input())
s = input()
print(n*s)

#38
a,b = map(int,input().split())
print(a**b)

#39
a, b = map(float,input().split())
print(a**b)

#40
a, b = map(int,input().split())
print(a//b)

#41
a, b = map(int,input().split())
print(a%b)

#42
a = float(input())
print(format(a,".2f"))

#43
a, b = map(float,input().split())
print(format(a/b, ".3f"))

#44
a, b = map(int,input().split())
print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a%b)
print(format(a/b,".2f"))

#45
a, b, c = map(int,input().split())
print(a+b+c, format((a+b+c)/3, ".2f"))

#46
a = int(input())
print(a<<1)

#47
a,b = map(int,input().split())
print(a<<b)

#48
a, b = map(int,input().split())
if a<b:
    print("True")
else:
    print("False")

#49
a, b = map(int,input().split())
if a==b:
    print("True")
else:
    print("False")

#50
a, b = map(int,input().split())
if b>=a:
    print("True")
else:
    print("False")