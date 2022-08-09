n = int(input())
time = list(map(int,input().split()))
time.sort()
summ = 0
for i in range(1,n):
    time[i] += time[i-1] + summ
print(sum(time))