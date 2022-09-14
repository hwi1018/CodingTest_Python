
import sys

word = sys.stdin.readline().rstrip()

length = len(word)

res = []
for i in range(1, length-1):
    for j in range(i+1, length):
        
        first = list(word[:i])
        second = list(word[i:j])
        third = list(word[j:])
        
        first.reverse()
        second.reverse()
        third.reverse()
        
        change_word = "".join(first+second+third) #리스트 데이터도 합칠 수 있음
        
        res.append(change_word)

print(min(res))
