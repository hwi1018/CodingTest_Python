n = int(input())
cm = []
stack = []
res = 0
for _ in range(n):
    cm.append(int(input()))


for i in range(len(cm)):
    while stack and (stack[-1][0] < cm[i]):
        res += stack.pop()[1]
    
    if not stack:
        stack.append((cm[i], 1))
        continue
    
    if stack[-1][0] == cm[i]:
        cnt = stack.pop()[1]
        res += cnt
        if stack:
            res += 1
        stack.append((cm[i], cnt+1))
    else:
        stack.append((cm[i], 1))
        res += 1

print(res)
