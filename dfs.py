
from collections import deque #bfs를 위한 deque

N, M, V = map(int, input().split())

#처음 0번째 추가
graph = []
for _ in range(N+1):
    graph.append([0]*(N+1))
    
for _ in range(M):
    m1, m2 = map(int, input().split())
    graph[m1][m2] = graph[m2][m1] = 1 #간선 정보 기입

def dfs(start, visited = []):
    visited.append(start)
    print(start, end=' ')
    
    #start 노드를 기준으로 간선 체크
    for w in range(len(graph[start])):
        if(graph[start][w] == 1 and (w not in visited)): #w정보가 visited에 없으면
            dfs(w, visited) #해당되는 w, 현재 visited 정보
            
def bfs(start):
    visited = [start] #처음 노드 넣기
    queue = deque()   #bfs를 위한 큐 만들기
    queue.append(start)
    
    while queue:
        v = queue.popleft() #큐에서 빼기
        print(v, end= ' ')
        
        for w in range(len(graph[v])):
            if(graph[v][w] == 1 and (w not in visited)):
                visited.append(w) #방문처리
                queue.append(w) #큐에 넣기
    
dfs(V)
print()
bfs(V)