import sys
import heapq

heap = []
n = int(sys.stdin.readline().rstrip())

for _ in range(n):
    x = int(sys.stdin.readline().rstrip())
    if x > 0:
        heapq.heappush(heap, x)
    elif x == 0:
        if heap == []:
            print(0)
        else:
            print(heap[0])
            heapq.heappop(heap)