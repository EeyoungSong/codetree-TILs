offset = 1000
MAX_NUM = 2000
grid = [[0] * MAX_NUM for _ in range(MAX_NUM)]



a, b, c, d = map(int, input().split())
for i in range(a, c):
    for j in range(b, d):
        grid[i+offset][j+offset] = 1

e, f, g, h = map(int, input().split())
for i in range(e, g):
        for j in range(f, h):
            grid[i+offset][j+offset] = 2

min_col, min_row = MAX_NUM, MAX_NUM
max_col, max_row = 0, 0

for i in range(0, MAX_NUM):
    for j in range(0, MAX_NUM):
        if grid[i][j] == 1:
            if min_row >= i:
                min_row = i
            if min_col >= j:
                min_col = j
            if max_row <= i:
                max_row = i
            if max_col <= j:
                max_col = j

cnt = 0
for elem in grid:
    cnt += elem.count(1)

if cnt == 0:
    print(0)
else:
    print((max_col - min_col + 1) * (max_row - min_row + 1))