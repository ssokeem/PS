n = int(input())

d= [1] * 10

for i in range(n - 1):
  for j in range(1, 10):
    d[j] += d[j - 1]

print(sum(d) % 10007)