
# 64 = 0100/0000
# 48 = 0011/0000
X = int(input())

cnt = 0
while X>0:
    
    if X&1 == 1:
        cnt+=1
    
    X>>=1
    
print(cnt)