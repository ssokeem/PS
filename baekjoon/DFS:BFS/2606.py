import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

dic = {}
visited = []

for i in range(n):
    dic[i+1] = set()

for j in range(m):
    a, b = map(int, input().split())
    dic[a].add(b)
    dic[b].add(a)

def dfs(start, dic):
    for i in dic[start]:
        if i not in visited:
            visited.append(i)
            dfs(i, dic)

dfs(1, dic)

print(len(visited)-1)