
T = int(input())

result = []
while T > 0:
    
    n = int(input())
    
    first_line = list(map(int, input().split()))
    second_line = list(map(int, input().split()))    
    
    for i in range(1, n):
        if i == 1:
            first_line[i] += second_line[0]
            second_line[i] += first_line[0]
        else:
            first_line[i] = max(second_line[i-2], second_line[i-1]) + first_line[i]
            second_line[i] = max(first_line[i-2],first_line[i-1]) +second_line[i]
    
    result.append(max(first_line[n-1], second_line[n-1]))
    
    T -= 1

for item in result:
    print(item)