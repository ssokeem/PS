import sys

k, n = map(int, sys.stdin.readline().split())
array = [int(sys.stdin.readline().rstrip()) for _ in range(k)]

start = 1
end = max(array)

result = 0

while(start <= end):
    count = 0
    mid = (start + end) // 2
    for x in array:
        count += x // mid
    if count < n:
        end = mid - 1
    else:
        start = mid + 1

print(end)
