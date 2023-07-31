num = set(range(1,10001))
generate_num = set()

for i in range(1,10001): # i=850
    for j in str(i): # j = "8","5","0"
        i += int(j)
    generate_num.add(i) #생성자가 있는 숫자들

self_num = sorted(num-generate_num)
for i in self_num:
    print(i)