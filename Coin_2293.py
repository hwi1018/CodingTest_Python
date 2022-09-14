
#반복된 형태인 함수로 만들 수 있는 경우
n, k = map(int, input().split())

coin_type = []
dp = [0]*(k+1)
for i in range(n):
    coin_type.append(int(input()))
    

dp[0] = 1

for i in range(0, n):
    for j in range(coin_type[i], k+1):
        dp[j] += dp[j-coin_type[i]]
        

print(dp[k])
