n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

ans = 0
for i in range(n):
    max_cnt = 0
    cnt = 1
    for j in range(1, n):
        if grid[i][j-1] == grid[i][j]:
            cnt += 1
        else:
            max_cnt = max(max_cnt, cnt)
            cnt = 1
    if cnt >= m:
        ans += 1

for j in range(n):
    max_cnt = 0
    cnt = 1
    for i in range(1, n):
        if grid[i][j] == grid[i-1][j]:
            cnt += 1
        else:
            max_cnt = max(max_cnt, cnt)
            cnt = 1
    if cnt >= m:
        ans += 1

print(ans)