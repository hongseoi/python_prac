def findKth(myInput, k):
    '''
    매 순간 k 번째로 큰 원소를 리스트로 반환
    '''
    result = []
    data = []

    for element in myInput:
        data.append(element)
        data.sort()

        '''
        data[k-1]이 우리가 찾는 값
        오류발생>> data안의 수 개수가 k보다 작을 때는?
        '''

        if len(data)<k:
            result.append(-1)
        else:
            result.append(data[k-1])
        
    return result

        

