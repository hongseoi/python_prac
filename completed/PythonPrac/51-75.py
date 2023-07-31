#51
from numpy import bitwise_and


a, b = map(int,input().split())
if a != b:
    print("True")
else:
    print("False")

#52
n = int(input())
print(bool(n))

#53
a = bool(int(input()))
print(not a)

#54
a, b = input().split()
print(bool(int(a)) and bool(int(b)))

#55
a, b = input().split()
print(bool(int(a)) or bool(int(b)))

#56
a, b = input().split()
c = bool(int(a))
d = bool(int(b))
print((c and (not d)) or ((not c) and d))

#57
a, b = map(bool, input().split())
if a == b:
    print("True")
else:
    print("False")

#57a
a, b = map(int, input().split())
c = bool(a)
d = bool(b)
if c == d:
    print("True")
else:
    print("False")

#58
a, b = map(int, input().split())
c = bool(a)
d = bool(b)
if c == False:
    if d == False:
        print("True")
    else:
        print("False")
else:
    print("False")

#58a
a,b = input().split()
c = bool(int(a))
d = bool(int(b))
print(not(c or d))

#58b
a,b = input().split()
c = bool(int(a))
d = bool(int(b))
print(c==False and d==False)

#59
'''
~   bitewise not
&   bitewise and
|   bitewise or
^   bitewise xor
<<  bitewise left shift
>>  bitewise right shift
'''
a = int(input())
print(~a)

#60
a,b = map(int, input().split())
print(a&b)

#61
a,b = map(int, input().split())
print(a|b)

#62
a,b = map(int, input().split())
print(a^b)

#63: 3항연산: x if C else y:
a,b = map(int, input().split())
print(a if (a>=b) else b)

#64
a,b,c = map(int,input().split())
print((a if a<b else b) if ((a if a<b else b)<c) else c)

#65
a,b,c = map(int,input().split())
if a%2==0:
    print(a)
if b%2==0:
    print(b)
if c%2==0:
    print(c)

#66
a,b,c = map(int,input().split())
if a%2==0:
    print("even")
else:
    print("odd")
if b%2==0:
    print("even")
else:
    print("odd")
if c%2==0:
    print("even")
else:
    print("odd")

#67
a = int(input())
if a<0:
    if a%2==0:
        print("A")
    else:
        print("B")
else:
    if a%2==0:
        print("C")
    else:
        print("D")

#68
a = int(input())
if a>=90:
    print("A")
else:
    if a>=70:
        print("B")
    else:
        if a>=40:
            print("C")
        else:
            print("D")

#69
n = input()
if n == "A":
    print("best!!!")
else:
    if n == "B":
        print("good!!")
    else:
        if n == "C":
            print("run!")
        else:
            if n == "D":
                print("slowly~")
            else:
                print("what?")

#70
month = int(input())
if month//3==1:
    print("spring")
else:
    if month//3==2:
        print("summer")
    else:
        if month//3==3:
            print("fall")
        else:
            print("winter")

#71
n=1
while n!=0:
    n=int(input())
    if n != 0:
        print(n)
    
#72
n = int(input())
while n!=0:
    print(n)
    n-=1

#73
n = int(input())
while n!=0:
    print(n-1)
    n-=1

#74
c = ord(input())
t = ord('a')
while t<=c:
    print(chr(t), end=" ")
    t+=1

#75
n = int(input())
for i in range(n+1):
    print(i)

