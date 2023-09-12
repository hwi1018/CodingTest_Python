n = int(input()) #탑의 수
h = [0] + list(map(int, input().split()))
result = [0] * (n+1)
stack = []

for i in range(1, n+1):
    while stack:
        if h[i] > stack[-1][0]:
            stack.pop()
        else:
            #현재 탐색하고 있는 탑의 높이가 TOP 보다 작다면
            result[i] = stack[-1][1]
            break
    
    stack.append((h[i], i))

for i in range(1, n+1):
    print(result[i], end = ' ')
