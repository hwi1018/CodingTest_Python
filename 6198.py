
n = int(input())
stack = []

buildings = []
result = 0

for i in range(n):
    buildings.append(int(input()))

for b in buildings:
    while stack and stack[-1] <= b:
        stack.pop()
    stack.append(b)

    result += len(stack)-1

print(result)
