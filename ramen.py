#i번 공장, 라면i , 3
#i, i+1, 5
#i, i+1, i+2 7

n = int(input())

A = list(map(int, input().split())) + [0,0]
#마지막에 0 2개 추가

ans = 0
for i in range(n):
    if( A[i+1] > A[i+2]):
        num = min(A[i], A[i+1]-A[i+2])    
        ans += 5*num
        A[i]-=num
        A[i+1] -= num
        
        num2 = min(A[i], min(A[i+1], A[i+2]))
        ans+=7*num2
        A[i] -=num2
        A[i+1] -=num2
        A[i+2] -=num2
    else:
        num2 = min(A[i], min(A[i+1], A[i+2]))
        ans+=7*num2
        A[i] -=num2
        A[i+1] -=num2
        A[i+2] -=num2
        
        num = min(A[i], A[i+1])    
        ans += 5*num
        A[i]-=num
        A[i+1] -= num
    
    ans += 3*A[i]
        
print(ans)