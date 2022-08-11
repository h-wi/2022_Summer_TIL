import sys
from collections import deque

n = int(sys.stdin.readline())
l1 = deque([]) 
for i in range(n):
    do = sys.stdin.readline().split()
    if do[0] == 'push':
        l1.append(do[1])
    elif do[0] == 'pop':
        if not l1:
            print('-1')
        else:
            print(l1.popleft())
    elif do[0] == 'size':
        print(len(l1)) 
    elif do[0] == 'empty':
        if len(l1) == 0: 
            print('1')
        else:
            print('0')
    elif do[0] == 'front':
        try:
            print(l1[0]) 
        except:
            print('-1')
    elif do[0] == 'back':
        try:
            print(l1[len(l1)-1])
        except:
            print('-1')
