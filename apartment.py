n = int(input())
adj_mat = [[0 for _ in range(n)] for _ in range(n)]
visited = [0 for _ in range(n+1)]
for i in range(n):
  insert = input()
  for j in range(n):
    adj_mat[i][j] = int(insert[j])
