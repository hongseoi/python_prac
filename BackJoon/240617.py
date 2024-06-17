"""_summary_
종말의 수: 6이 3개 이상 연속으로 들어가는 수(ex 666, 1666, ..., 6666, 6661)
N번째 종말의 수: N번째로 작은 종말의 수
"""

def is_end_num(number):
    return '666' in str(number)   
 
def find_number(N):
   count = 0
   number = 665
   
   while count < N:
       number +=1
       if is_end_num(number):
           count += 1
   return number

n = int(input("몇번째 종말의 수?"))
print(find_number(n))