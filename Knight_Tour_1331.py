
# KNight Tour

from collections import deque

board = []

queue = deque()
for i in range(36):
    pos = input()
    pos_list = list(pos)

    x = ord(pos[0]) - 65
    y = int(pos[1]) - 1

    board.append(pos)
    queue.append([x, y])

knight_moves = [[1, 2], [2, 1], [2, -1], [1, -2],
                [-1, -2], [-2, -1], [-2, 1], [-1, 2]]

validFlag = False

start_x, start_y = queue.popleft()
queue.append([start_x, start_y])

if len(set(board)) == 36:
    while queue:
        validFlag = False

        x, y = queue.popleft()

        dx = x - start_x
        dy = y - start_y

        start_x = x
        start_y = y

        for move in knight_moves:
            if move == [dx, dy]:
                validFlag = True
                break

        if validFlag is not True:
            break

    if validFlag:
        print('Valid')
    else:
        print('Invalid')
else:
    print('Invalid')


