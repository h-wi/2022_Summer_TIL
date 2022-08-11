import sys
from collections import deque

n,k = map(int,input().split())
l1 = deque([i+1 for i in range(n)])
result = []

while not l1:
  result.append(l1[k])
  l1.remove(l1[k])
  k = (k+2) % len(l1)
print(result)
