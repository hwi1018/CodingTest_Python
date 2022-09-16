
N = int(input())

rgb_price = []

for i in range(N):
    rgb_price.append(list(map(int, input().split())))

min_price = [[0]*3 for _ in range(N)]

for i in range(N):

    if i == 0:
        min_price[i][0] = rgb_price[i][0]
        min_price[i][1] = rgb_price[i][1]
        min_price[i][2] = rgb_price[i][2]
    else:
        min_price[i][0] = rgb_price[i][0] + min(min_price[i-1][1], min_price[i-1][2])
        min_price[i][1] = rgb_price[i][1] + min(min_price[i - 1][0], min_price[i - 1][2])
        min_price[i][2] = rgb_price[i][2] + min(min_price[i - 1][0], min_price[i - 1][1])

print(min(min_price[-1]))