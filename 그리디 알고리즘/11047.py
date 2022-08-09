n,k = map(int, input().split())
coin = []
for i in range(n):
    type = input()
    coin.append(int(type))
coin.reverse()
count = 0
for j in range(n):
    while coin[j] <= k:
        count +=  k // coin[j]  #빼기로 하면 틀린다!!
        k %= coin[j]
print(count) 