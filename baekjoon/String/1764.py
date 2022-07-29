n, m = map(int, input().split())
no_listen = []
no_see = []

for i in range(n):
  no_listen.append(input())
    
for j in range(m):
  no_see.append(input())

bothno = sorted(set(no_listen).intersection(set(no_see)))

print(len(bothno))
for k in bothno:
  print(k)