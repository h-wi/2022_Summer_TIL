import sys
from collections import deque

n = int(sys.stdin.readline())
l1 = deque([n-i for i in range(n)])

while len(l1) > 1:
  l1.pop()
  l1.appendleft(l1.pop())
print(l1[0])
