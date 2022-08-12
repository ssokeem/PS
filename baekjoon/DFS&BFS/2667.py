import sys

n = int(sys.stdin.readline().rstrip())

graph = []
for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().rstrip())))
    
cnt_lst = []

def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False
    if graph[x][y] == 1:
        graph[x][y] = 0
        global cnt
        cnt += 1
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False

cnt = 0
result = 0

for i in range(n):
    for j in range(n):
        if dfs(i, j) == True:
            result += 1
            cnt_lst.append(cnt)
            cnt = 0

cnt_lst.sort()
print(result)
for i in range(len(cnt_lst)):
	print(cnt_lst[i])