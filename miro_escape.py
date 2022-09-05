from collections import deque

n, m = map(int, input().split())

miro = []
for i in range(n):
    miro.append(list(map(int, input())))

dx =[-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x,y))
    
    while queue:
        x,y = queue.popleft()
        
        for i in range(4):
            rx = x + dx[i]
            ry = y + dy[i]
            
            if rx <= -1 or ry <= -1 or rx >= n or ry >=m :
                continue
            
            if miro[rx][ry] == 0:
                continue
            
            if miro[rx][ry] == 1:
                miro[rx][ry] = miro[x][y] + 1
                queue.append((rx, ry))
    
    print(miro[n-1][m-1])
                  
bfs(0,0)
//HIHIHI
