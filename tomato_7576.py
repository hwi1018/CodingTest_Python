from collections import deque

#주변의 토마토를 익게하는 bfs문제
m, n = map(int, input().split())
res = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

tomato_box = []
for i in range(n):
    tomato_box.append(list(map(int, input().split())))

queue = deque()
#토마토 좌표를 저장
for i in range(n):
    for j in range(m):
        if tomato_box[i][j] == 1:
            queue.append([i, j])

def FindTomatoFinishedDay():
    while queue:
        x, y = queue.popleft()

        #상하좌우 비교
        for i in range(4):
            rx = x + dx[i]
            ry = y + dy[i]

            if rx < 0 or rx >= n or ry < 0 or ry >= m:
                continue

            #주변 토마토가 0일 때
            if tomato_box[rx][ry] == 0:
                tomato_box[rx][ry] = tomato_box[x][y] + 1
                queue.append([rx, ry])

FindTomatoFinishedDay()

for tomato_line in tomato_box:
    for tomato in tomato_line:
        if tomato == 0:
            print(-1)
            exit(0)

    res = max(res, max(tomato_line))

print(res - 1)
