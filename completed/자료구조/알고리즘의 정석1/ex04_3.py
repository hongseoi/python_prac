'''
Fractional knapsack
nnn개의 물건이 있고, 각 물건은 무게 wiw_iw 
i
​
 와 가치 cic_ic 
i
​
 를 갖는다. 이제 이 물건들을 배낭에 넣으려 한다. 이 배낭은 무게 mmm까지를 버틸 수 있다.

한 가지 재미있는 사실은, 물건을 쪼갤 수 있다는 것이다. 물론, 물건을 쪼개게 되면 무게가 줄지만, 가치도 줄게 된다. 예를 들어, 무게를 절반으로 줄이면 가치 역시도 절반으로 줄어들게 된다.

배낭이 버틸 수 있는 무게 mmm과 nnn개의 물건의 정보가 주어질 때, 배낭이 담을 수 있는 가치의 최댓값을 소숫점 넷째자리에서 반올림하여 출력하는 프로그램을 작성하세요.

입력에 첫줄에는 물건의 개수nnn과 배낭이 버틸 수 있는 무게 mmm이 입력됩니다.

이후 nnn개의 줄에 대하여 각 물건의 무게 wiw_iw 
i
​
 , 그리고 가치 cic_ic 
i
​
 가 주어진다.
'''


import sys

def fKnapsack(materials, m) :
    '''
    크기 m까지 버틸 수 있는 베낭이 담을 수 있는 최대 가치를 반환하는 함수를 작성하세요.

    주의 : 셋째 자리에서 반올림하는 것을 고려하지 않고 작성하셔도 됩니다. 
    
    물건 쪼개기 가능
    물건을 가성비순으로 넣기
    
    x in materials
    x[0]: 무게
    x[1]: 가치
    '''
    
    materials = sorted(materials, key=lambda x: x[1]/x[0], reverse=True)
    
    weight = 0
    value = 0
    
    for i in range(len(materials)):
        '''
        1. 물건을 넣어도 아직 최대 무게보다 적을 때
        2. 물건 넣으면 딱 m만큼의 무게가 될때
        3. 물건을 다 넣으면 m 초과
        '''
        
        if weight + materials[i][0] < m:
            weight += materials[i][0]
            value += materials[i][1]
        elif weight + materials[i][0] == m:
            weight + materials[i][0]
            value += materials[i][1]
            
            return value
        else:
            temp = m - weight
            value += temp * (materials[i][1]/materials[i][0])
            return value
    
    
    

    return value

def main():
    '''
    이 부분은 수정하지 마세요.
    '''

    line = [int(x) for x in input().split()]

    n = line[0]
    m = line[1]

    materials = []

    for i in range(n) :
        data = [int(x) for x in input().split()]
        materials.append( (data[0], data[1]) )

    print("%.3lf" % fKnapsack(materials, m))

if __name__ == "__main__":
    main()
