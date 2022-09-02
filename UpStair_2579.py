#10, 20, 15, 25, 10, 20
#연속 3개 안됨

N = int(input())

stairs = [0]*300
for i in range(N):
    stairs.insert(i, int(input()))

score = [0]*300
score[0] = stairs[0]#1칸
score[1] = max(stairs[0] + stairs[1], stairs[1])#2칸
score[2] = max(stairs[0]+stairs[2], stairs[1]+stairs[2])#3칸

for i in range(3, N):
    score[i] = max(score[i-2]+stairs[i], 
                   score[i-3]+ stairs[i]+stairs[i-1])

print(score[N-1])


