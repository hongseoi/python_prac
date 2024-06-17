N = int(input())
lst = list(map(int,input().split()))
mx = max(lst)
new_lst = lst/mx*100
avg = sum(new_lst)/N
print(avg)