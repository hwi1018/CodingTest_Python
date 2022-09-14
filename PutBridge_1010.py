
# 조합의 개념이 필요
# nCr = n!/ r!(r-n)!

import math

T = int(input())

for i in range(T):
    n, m = map(int, input().split())
    bridge = int(math.factorial(m) / (math.factorial(n) * math.factorial(m-n)))
    print(bridge)

