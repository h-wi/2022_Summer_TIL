import sys
sys.setrecursionlimit(10**6)

global c
c = 1
def dfs(adjac_lst,r):
    global c
    visited[r-1] = c
    for i in adjac_lst[r-1]:
        if not visited[i-1]:
            c += 1
            dfs(adjac_lst,i)

n,m,r = map(int,input().split())
edges = []
adjac_lst = [[] for vertex_number in range(n)] #adjacent list를 만들기 위해 vertex의 갯수만큼 미리 리스트 생성
visited = [0 for visit in range(n)]

for i in range(m):
    u,v = map(int,input().split())
    edges.append((u,v)) #tuple형태로 edge를 받아준다

edges.sort(key=lambda x: x[1]) #vertex를 오름차순으로 방문하기 위해 정렬

for edge in edges:
    adjac_lst[edge[0]-1].append(edge[1])
    adjac_lst[edge[1]-1].append(edge[0]) #undirected edge이므로 번갈아 추가

dfs(adjac_lst,r)

for i in visited:
    print(i)


