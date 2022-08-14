def binary_search(arr,target,start,end): #binary search에서 중복 횟수를 찾으면 시간초과
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return hash[target]
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
 
n = int(input())
lst = list(map(int,input().split()))
m = int(input())
check = list(map(int,input().split()))

hash = {} #dictionary를 이용해서 얼마나 중복됐는지 미리 저장 

for i in lst:
    if i in hash:
        hash[i] += 1
    else:
        hash[i] = 1

lst.sort()
for i in range(m):
    result = binary_search(lst,check[i],0,n-1)
    if result:
        print(result, end = ' ')
    else:
        print(0, end = ' ')
