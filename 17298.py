import sys
from collections import deque
n = int(input())
A = list(map(int, sys.stdin.readline().rstrip().split()))

q = deque()
result = [-1] * n

# O(N) 방법
for i in range(n):
    while q and (q[-1][0] < A[i]):
        val,idx = q.pop()
        result[idx] = A[i]
    
    q.append((A[i], i))

for res in result:
    print(res, sep=' ')
