from collections import deque
import sys

n, m = map(int, sys.stdin.readline().split())

gp = []
for i in range(n):
    gp.append(list(map(int, sys.stdin.readline().rstrip())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue

            if gp[nx][ny] == 0:
                continue

            if gp[nx][ny] == 1:
                gp[nx][ny] = gp[x][y] + 1

                queue.append((nx, ny))
            
    return gp[n-1][m-1]

print(bfs(0, 0))