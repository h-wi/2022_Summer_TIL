import sys
import heapq

n = int(input())
min_heap = []
for i in range(n):
    num = int(sys.stdin.readline())
    if num:
        heapq.heappush(min_heap,num)
    else:
        try:
            print(heapq.heappop(min_heap))
        except:
            print(0)