import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
count = 0

visited = [False] * (n + 1)
gp = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    gp[a].append(b)
    gp[b].append(a)

def bfs(start):
    queue = deque([start])
    visited[start] = True
    
    while queue:
        x = queue.popleft()
        for i in gp[x]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)

for j in range(1, n + 1):
    if not visited[j]:
        if not gp[j]:
            count += 1
            visited[j] = True
        else:
            bfs(j)
            count += 1

print(count)