
n = int(input())

cur = 1
flag = 0
stack = []
answer = []
for _ in range(n):
    m = int(input())
    while cur <= m:
        stack.append(cur)
        answer.append('+')
        cur += 1
    
    if stack[-1] == m:
        stack.pop()
        answer.append('-')
    else:
        print('NO')
        flag = 1
        break

if flag == 0:
    for c in answer:
        print(c)    
