n = int(input())
grid = [[0] * n for _ in range(n)]

drs, dcs = [0, 1, 0, -1], [1, 0, -1, 0]
dir_num = 0 

cnt = 1
r, c = n//2, n//2
grid[r][c] = 1
for i in range(1, n):
    for j in range(2):
        for k in range(i):
            cnt += 1
            r, c = r + drs[dir_num], c + dcs[dir_num]
            grid[r][c] = cnt 
        dir_num = (dir_num - 1) % 4

for i in range(n-1):
    cnt += 1
    r, c = r + drs[dir_num], c + dcs[dir_num]
    grid[r][c] = cnt 

for i in range(n):
    for j in range(n):
        print(grid[i][j], end=" ")
    print()