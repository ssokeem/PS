import sys
from collections import deque

dx = [1, -1, 0, 0, 1, -1, 1, -1]
dy = [0, 0, -1, 1, -1, 1, 1, -1]

def bfs(x, y):
    
    gp[x][y] = 0
    queue = deque()
    queue.append((x, y))
    
    while queue:
        x, y = queue.popleft()
        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]
            
            if nx < 0 or nx >= h or ny < 0 or ny >= w:
                continue
            
            if gp[nx][ny] == 1:
                gp[nx][ny] = 0
                queue.append((nx, ny))

while True:
    w, h = map(int, sys.stdin.readline().split())
    
    if w == 0 and h == 0:
        break
    
    count = 0
    gp = []
    for _ in range(h):
        gp.append(list(map(int, sys.stdin.readline().split())))
        
    for i in range(h):
        for j in range(w):
            if gp[i][j] == 1:
                bfs(i, j)
                count += 1
                
    print(count)