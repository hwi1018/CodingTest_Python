
N = int(input())

words = []

for i in range(N):
    words.append(input())

words = list(set(words))

results = []

for word in words:
    results.append((len(word), word))

#글자 수에 따라 정렬
results = sorted(results)

for l, word in results:
    print(word)
