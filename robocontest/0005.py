import math

z = int(input())

if z==0:
    print(-1)
for d in range(1, int(math.isqrt(abs(z)))+1):
    if z % d == 0:
        x1, y1 = d, z//d
        if x1 <= y1:
            cnt = 0

