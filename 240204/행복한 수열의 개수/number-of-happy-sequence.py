n, m = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]
ans = 0

for i in range(n):
    p = grid[i][0]
    cnt = 1
    for j in range(1, n):
        if p == grid[i][j]:
            cnt += 1
        p = grid[i][j]
    if cnt >= m:
        ans += 1    

for j in range(n):
    p = grid[0][j]
    cnt = 1
    for i in range(1, n):
        if p == grid[i][j]:
            cnt += 1
        p = grid[i][j]
        #print(p)
    if cnt >= m:
        ans += 1

print(ans)