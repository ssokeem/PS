import sys
import heapq

heap = []
n = int(sys.stdin.readline())

for _ in range(n):
    heapq.heappush(heap, int(sys.stdin.readline()))

if len(heap) == 1:
    print(0)
else:
    result = 0
    while len(heap) > 1:
        minsum = heapq.heappop(heap) + heapq.heappop(heap)
        result += minsum
        heapq.heappush(heap, minsum)
        
    print(result)