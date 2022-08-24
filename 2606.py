v = int(input())
e = int(input())
adj_mat = [[0 for _ in range(v)] for _ in range(v)]
visited = [0 for _ in range(v+1)]
for _ in range(e):
  u,v = map(int,input().split())
  adj_mat[u-1][v-1] = 1
  adj_mat[v-1][u-1] = 1
def dfs(adj_mat,r):
  visited[r] = 1
  for i in adj_mat[r-1]:
    if adj_mat[r-1][i-1] != 0 and not visited[i]:
      dfs(adj_mat,i)
dfs(adj_mat,1)
count = 0
for j in range(1,v+1):
  if visited[j]:
    count += 1
print(count)


  # for p in range(v):
  #   for q in range(v):
  #     print(adj_mat[p][q], end = ' ')
  #   print()
