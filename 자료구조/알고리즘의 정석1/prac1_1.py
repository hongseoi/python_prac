#재귀호출을 이용해 10진수 >> 2진수
import sys
sys.setrecursionlimit(100000)

def convertBinary(n) :
    '''
    10진수 n을 2진수로 변환하여 반환합니다.

    *주의* : 변환된 2진수는 문자열이어야 합니다.

    예를 들어, 19가 입력될 경우 문자열 "10011"이 반환되어야 합니다.
     n//2 몫
    n%2 나머지
    '''
    if n//2 <= 1:
        return num
        
    num = ''
    
    n1 = n%2
    num.append(n1)
    
    n2 = n//2
    if n2//2 >=2:
     nums.append("0")
   

    return "0"

def main():

    n = int(input())

    print(convertBinary(n))

if __name__ == "__main__":
    main()
