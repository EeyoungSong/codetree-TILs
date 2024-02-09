n, r, c = map(int, input().split())
r, c = r-1, c-1
grid = [list(map(int, input().split())) for _ in range(n)]


def find_bigger(r, c):
    drs, dcs = [-1, 1, 0, 0], [0, 0, -1, 1]
    for dr, dc in zip(drs, dcs):
        nr, nc = r + dr, c + dc
        if in_range(nr, nc) and grid[nr][nc] > grid[r][c]:
            r, c = nr, nc
            break
    return r, c

def in_range(r, c):
    return 0 <= r < n and 0 <= c < n

print(grid[r][c], end=" ")
while True:
    nr, nc = find_bigger(r, c)
    if r == nr and c == nc:
        break
    else:
        r, c = nr, nc
        print(grid[r][c], end=" ")