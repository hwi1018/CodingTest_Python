
import sys
from collections import deque

n, m = map(int, input().split())

board = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n):
    board.append(list(input()))
    for j in range(m):
        if board[i][j] == 'R':
            Rx, Ry = i, j
        elif board[i][j] == 'B':
            Bx, By = i, j


def Move(rx, ry, bx, by):
    queue = deque()
    queue.append((rx, ry, bx, by))

    visited = []
    visited.append((rx, ry, bx, by))

    count = 0
    while queue:
        for _ in range(len(queue)):
            rx, ry, bx, by = queue.popleft()

            if count > 10:
                break

            if board[rx][ry] == 'O':
                print(count)
                return

            for i in range(4):
                nrx, nry = rx, ry
                while True:
                    nrx += dx[i]
                    nry += dy[i]

                    if board[nrx][nry] == '#':
                        nrx -= dx[i]
                        nry -= dy[i]
                        break

                    if board[nrx][nry] == 'O':
                        break

                nbx, nby = bx, by
                while True:
                    nbx += dx[i]
                    nby += dy[i]

                    if board[nbx][nby] == '#':
                        nbx -= dx[i]
                        nby -= dy[i]
                        break

                    if board[nbx][nby] == 'O':
                        break

                #파란공이 먼저 들어오면 무시
                if board[nbx][nby] == 'O':
                    continue

                # 같은 지점일때
                if nrx == nbx and nry == nby:
                    #더 많이 이동한 구슬
                    if abs(nrx - rx) + abs(nry - ry) > abs(nbx - bx) + abs(nby - by):
                        nrx -= dx[i]
                        nry -= dy[i]
                    else:
                        nbx -= dx[i]
                        nby -= dy[i]

                if (nrx, nry, nbx, nby) not in visited:
                    queue.append((nrx, nry, nbx, nby))
                    visited.append((nrx, nry, nbx, nby))
        count += 1
    print(-1)

# 현재 빨간공, 파란공 좌표 넣기
Move(Rx, Ry, Bx, By)