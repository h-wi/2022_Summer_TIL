def binary_search(arr,target,start,end):

    if start > end:
        return 0
    mid = (start + end) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        binary_search(arr,target,start,mid-1)
    else:
        binary_search(arr,target,mid+1,end)

n = int(input())
lst = list(map(int,input().split()))
m = int(input())
check = list(map(int,input().split()))

lst.sort()
for i in range(m):
    count = 0
    while binary_search(lst,check[i],0,len(lst)-1) != 0:
        count += 1
        try:
            lst.remove(check[i])
        except:
            break
    print(count-1, end=' ')
