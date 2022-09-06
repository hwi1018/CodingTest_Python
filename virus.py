
#네트워크 상으로 연결되어있으면 다 감염 1
#다른 네트워크 0

N = int(input()) #컴퓨터의 수

M = int(input()) #네트워크 상 연결되어있는 쌍 수

nets = [[]* N for _ in range(N+1)]
visited = [0] * (N+1)
for i in range(M):
    a,b = map(int, input().split())
    nets[a].append(b)
    nets[b].append(a)
    
cnt = 0

def dfs(start):
    global cnt
    visited[start] = 1
    
    for i in nets[start]:
        if(visited[i] == 0):#방문하지 않은 애들
            dfs(i)
            cnt += 1
            
dfs(1)

print(cnt)
