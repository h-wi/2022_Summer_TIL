import sys
from collections import deque

n,k = map(int,input().split())
l1 = deque([i+1 for i in range(n)])
result = []
k -= 1 
there = k

while l1:
  result.append(str(l1[k]))
  l1.remove(l1[k])
  if len(l1) == 0:
    break
  k = (k+there) % len(l1)

print('<', ", ".join(result), '>' , sep='')
