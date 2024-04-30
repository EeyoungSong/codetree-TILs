n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

def in_range(r, c):
    return 0 <= r < n and 0 <= c < n

def block1(r, c):
    arr1 = ([0, 0, -1], [0, 1, 0])
    arr2 = ([0, 0, 1], [0, 1, 0])
    arr3 = ([0, 1, 0], [0, 0, -1])
    arr4 = ([0, 0, -1], [0, -1, 0])
    arrs = [arr1, arr2, arr3, arr4]

    max_num = 0
    for i in range(4):
        drs, dcs = arrs[i]
        s = 0
        for dr, dc in zip(drs, dcs):
            nr, nc = r + dr, c + dc
            if not in_range(nr, nc):
                s = 0
                break
            else:
                s += grid[nr][nc]
        max_num = max(max_num, s)
    return max_num
        

def block2(r, c):
    arr1 = ([0, 0, 0], [0, 1, 2])
    arr2 = ([0, 1, 2], [0, 0, 0])
    arrs = [arr1, arr2]

    max_num = 0
    for i in range(2):
        drs, dcs = arrs[i]
        s = 0
        for dr, dc in zip(drs, dcs):
            nr, nc = r + dr, c + dc
            if not in_range(nr, nc):
                s = 0
                break
            else:
                s += grid[nr][nc]
        max_num = max(max_num, s)
    return max_num

ans = 0
for i in range(n):
    for j in range(n):
        t = max(block1(i, j), block2(i, j))
        ans = max(ans, t)
print(ans)