n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
temp = [[0]*n for _ in range(n)]

r, c = map(int, input().split())


drs, dcs = [0, 1, 0, -1], [1, 0, -1, 0]

def in_range(r, c):
    return 0 <= r < n and 0 <= c < n

r, c = r-1, c-1
for dr, dc in zip(drs, dcs):
    tr, tc = r, c
    for _ in range(grid[r][c]-1):
        nr, nc = tr + dr, tc + dc
        if in_range(nr, nc):
            grid[nr][nc] = 0
            tr, tc = nr, nc

grid[r][c] = 0


temp = [[0] * n for _ in range(n)]

for j in range(n):
    row = n-1
    temp_row = n-1
    # for i in range(n-1, -1, -1):
    #     if grid[i][j] != 0:
    #         grid[temp_row][j] = grid[i][j]
    #         temp_row -= 1

    while row >= 0:
        if grid[row][j] != 0:
            temp[temp_row][j] = grid[row][j]
            temp_row -= 1
        row -= 1

for arr in temp:
    for elem in arr:
        print(elem, end=" ")
    print()