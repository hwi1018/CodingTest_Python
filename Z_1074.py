
import math

n, r, c = map(int, input().split())

def SearchZ(n, r, c):
    if n == 0:
        return 0

    half = 1 << (n-1) #절반

    if (r < half and c < half):
        return SearchZ(n-1, r, c)

    if (r < half and c >= half):
        return math.pow(half, 2) + SearchZ(n-1, r, c-half)

    if (r >= half and c < half):
        return 2*math.pow(half, 2) + SearchZ(n-1, r-half, c)

    return 3 * math.pow(half, 2) + SearchZ(n-1, r-half, c-half)

print(int(SearchZ(n, r, c)))
