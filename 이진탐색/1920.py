n = int(input())
num_set = set(map(int,input().split()))
m = int(input())
check = list(map(int,input().split()))

for i in range(m):
    if check[i] in num_set:
        check[i] = 1
    else:
        check[i] = 0
    print(check[i])