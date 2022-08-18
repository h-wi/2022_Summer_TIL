import sys
import heapq

max = []
min = []
n = int(input())
for i in range(n):
  num = int(sys.stdin.readline())
  if num > 0:
    heapq.heappush(min,num)
  elif num < 0:
    heapq.heappush(max,(-num,num))
  else:
    try:
      min_item = min[0]
      max_item = max[0][1]

      if min_item < abs(max_item):
        print(heapq.heappop(min))
      else:
        print(heapq.heappop(max)[1])
    except IndexError:
      if len(min) == 0 and len(max) != 0:
        print(heapq.heappop(max)[1])
      elif len(min) != 0 and len(max) == 0:
        print(heapq.heappop(min))
      else:
        print(0)
