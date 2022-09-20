import sys
from collections import deque

n = int(input())

board = []
for _ in range(n):
    board.append(list(map(int, sys.stdin.readline().rstrip())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(board, x, y):
    queue = deque()
    queue.append([x, y])
    board[x][y] = 0 # 0으로 바꿔주기
    count = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 1:
                board[nx][ny] = 0
                queue.append([nx, ny])
                count += 1
    return count

result = []
for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            apart_cnt = bfs(board, i, j)
            result.append(apart_cnt)

print(len(result))

result.sort()
for res in result:
    print(res)

