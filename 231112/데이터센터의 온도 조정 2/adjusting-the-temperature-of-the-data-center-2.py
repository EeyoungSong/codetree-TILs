n, c, g, h = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

max_e = 0
for t in range(0, 1001):
    e = 0
    for ta, tb in arr:
        if t < ta:
            e += c
        elif ta <= t <= tb:
            e += g
        elif t > tb:
            e += h
    max_e = max(max_e, e)
print(max_e)