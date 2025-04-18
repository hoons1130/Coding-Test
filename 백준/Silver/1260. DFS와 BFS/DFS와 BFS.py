from collections import deque
n, m, v = map(int, input().split())
matrix = [[0]*(n+1) for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    f, t = map(int, input().split())
    matrix[f][t] = matrix[t][f] = 1

def dfs(matrix, v, visited):
    print(v, end=' ')
    visited[v] = True
    for i in range(len(matrix[v])):
        if matrix[v][i] == 1 and visited[i] == False:
            dfs(matrix, i, visited)
dfs(matrix, v, visited)
print()
visited = [False] * (n+1)

def bfs(matrix, v, visited):
    queue = deque()
    queue.append(v)
    while queue:
        value = queue.popleft()
        if visited[value] == False:
            print(value, end=' ')
            visited[value] = True
            for i in range(len(matrix[value])):
                if matrix[value][i] == 1 and visited[i] == False:
                    queue.append(i)
bfs(matrix, v, visited)