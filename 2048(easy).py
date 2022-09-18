
from copy import deepcopy

data = []
answer = 0

n = int(input())
for _ in range(n):
    data.append(list(map(int, input().split())))

def Up(board):
    for j in range(n):
        pointer = 0
        for i in range(1, n):
            if board[i][j]:
                tmp = board[i][j]
                board[i][j] = 0
                # 포인터가 가리키는 수가 0일 때
                if board[pointer][j] == 0:
                    board[pointer][j] = tmp
                # 포인터가 가리키는 수와 현재 위치의 수가 같을 때
                elif board[pointer][j]  == tmp:
                    board[pointer][j] *= 2
                    pointer += 1
                # 포인터가 가리키는 수와 현재 위치의 수가 다를 때
                else:
                    pointer += 1
                    board[pointer][j] = tmp
    return board

def Down(board):
    for j in range(n):
        pointer = n-1
        for i in range(n-2, -1, -1):
            if board[i][j]:
                tmp = board[i][j]
                board[i][j] = 0

                if board[pointer][j] == 0:
                    board[pointer][j] = tmp
                elif board[pointer][j] == tmp:
                    board[pointer][j] *= 2
                    pointer -= 1
                else:
                    pointer -= 1
                    board[pointer][j] = tmp
    return board

def Left(board):
    for i in range(n):
        pointer = 0
        for j in range(1, n):
            if board[i][j]:
                tmp = board[i][j]
                board[i][j] = 0

                if board[i][pointer] == 0:
                    board[i][pointer] = tmp
                elif board[i][pointer] == tmp:
                    board[i][pointer] *= 2
                    pointer += 1
                else:
                    pointer += 1
                    board[i][pointer] = tmp
    return board


def Right(board):
    for i in range(n):
        pointer = n-1

        for j in range(n-2, -1, -1):
            if board[i][j]:
                tmp = board[i][j]
                board[i][j] = 0

                if board[i][pointer] == 0:
                    board[i][pointer] = tmp
                elif board[i][pointer] == tmp:
                    board[i][pointer] *= 2
                    pointer -= 1
                else:
                    pointer -= 1
                    board[i][pointer] = tmp
    return board


def Move(board, cnt):
    global answer
    if cnt == 5:
        for i in range(n):
            for j in range(n):
                answer = max(answer, board[i][j])
        return

    #원본을 훼손시키지 않기 위해
    Move(Up(deepcopy(board)), cnt+1)
    Move(Down(deepcopy(board)), cnt + 1)
    Move(Left(deepcopy(board)), cnt + 1)
    Move(Right(deepcopy(board)), cnt + 1)

Move(data, 0)

print(answer)

