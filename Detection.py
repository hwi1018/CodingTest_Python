# 이진 탐색(탐색범위를 절반씩 좁히기) 
# 시간복잡도 log₂N 보장
# start, end, mid 설정(index)
# 찾고자 하는 값과 중간값을 비교

#1) 재귀적으로 구현

n, target = list(map(int, input().split()))

array = list(map(int, input().split()))

# mid값을 찾아서 target값과 비교 후 재귀 진행
def binary_search(array, target, start, end):
    if start>end:
        return
    mid = (start+end)//2
    
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    else:
        return binary_search(array,target, mid+1, end)

result = binary_search(array, target, 0 , n-1)

if result == None:
    print('원소 없음')
else:
    print(result+1)

