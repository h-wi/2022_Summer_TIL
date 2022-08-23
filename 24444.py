import sys
from collections import deque

n,m,r = map(int, sys.stdin.readline().split())
adj_lst = [[] for vertex in range(n)]
visited = [0] * (n+1)
now = deque([]); count = 1
for edge in range(m):
    u,v = map(int, sys.stdin.readline().split())
    adj_lst[u-1].append(v)
    adj_lst[v-1].append(u)
for vertex in range(n):
    adj_lst[vertex].sort() # 24444
    # adj_lst[vertex].sort(reverse=True) 24445

def bfs(adj_lst,r):
    global count
    visited[r] = count
    count += 1

    now.append(r)

    while(now):
        num = now.popleft()
        for vertex in adj_lst[num-1]:
            if not visited[vertex]:
                visited[vertex] = count
                count += 1
                now.append(vertex)

        
bfs(adj_lst,r)
for result in range(1,n+1):
    print(visited[result])