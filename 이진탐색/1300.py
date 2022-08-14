n = int(input())
lst = [i*j for i in range(1,n+1)
 for j in range(1,n+1)]
k = int(input())
print(lst[k])

#메모리 초과
