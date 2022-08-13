import bisect

n = int(input())
lst = list(map(int,input().split()))
m = int(input())
check = list(map(int,input().split()))

lst.sort()
for i in range(m):
    count = bisect.bisect_right(lst,check[i])-bisect.bisect_left(lst,check[i])
    print(count, end=' ')
