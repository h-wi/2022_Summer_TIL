import sys
sys.setrecursionlimit(10**6)
n,m,r = map(int,sys.stdin.readline().split())
adj_lst = [[] for vertex in range(n)]
visited = [0 for _ in range(n+1)]; count = 1
for edge in range(m):
  u,v = map(int,sys.stdin.readline().split())
  adj_lst[u-1].append(v)
  adj_lst[v-1].append(u)
for vertex in range(n):
  adj_lst[vertex].sort()

def dfs(adj_lst,r):
  global count
  visited[r] = count
  count += 1
  for i in adj_lst[r-1]:
    if not visited[i]:
      dfs(adj_lst,i)
dfs(adj_lst,r)
for i in range(1,n+1):
  print(visited[i])
