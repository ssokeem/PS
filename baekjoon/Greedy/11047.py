import sys

n, k = map(int, sys.stdin.readline().split())
coin_types = [int(sys.stdin.readline()) for _ in range(n)]

count = 0
coin_types.sort(reverse=True)

for coin in coin_types:
  count += k // coin
  k %= coin

print(count)