import sys
from collections import deque
n,m,r = map(int,sys.stdin.readline().split())
adj_lst = [[] for _ in range(n)]
bfs_visited = [0 for _ in range(n+1)]; now = deque([])
dfs_visited = [0 for _ in range(n+1)];
for _ in range(m):
  u,v = map(int,sys.stdin.readline().split())
  adj_lst[u-1].append(v)
  adj_lst[v-1].append(u)
  
for i in range(n):
  adj_lst[i].sort()
  
def bfs(adj_lst,r):
  print(r, end = ' ')
  bfs_visited[r] = 1
  now.append(r)
  while now:
    key = now.popleft()
    for i in adj_lst[key-1]:
      if not bfs_visited[i]:
        print(i, end = ' ')
        bfs_visited[i] = i
        now.append(i)
def dfs(adj_lst,r):
  print(r, end = ' ')
  dfs_visited[r] = r

  for i in adj_lst[r-1]:
    if not dfs_visited[i]:
      dfs(adj_lst,i)

dfs(adj_lst,r)
print()
bfs(adj_lst,r)
