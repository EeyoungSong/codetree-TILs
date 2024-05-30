n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]

def in_range(r, c):
    return 0 <= r < n and 0 <= c < n

def can_go(r, c):
    if in_range(r, c) and visited[r][c] == 0 and grid[r][c] == num:
        return True
    return

def dfs(r, c):
    global cnt
    drs, dcs = [0, 1, 0, -1], [1, 0, -1, 0]
    for dr, dc in zip(drs, dcs):
        nr, nc = r + dr, c + dc
        if can_go(nr, nc):
            cnt += 1
            visited[nr][nc] = 1
            dfs(nr, nc)

ans = 0
max_cnt = 0
for i in range(n):
    for j in range(n):
        cnt = 0
        if in_range(i, j) and visited[i][j] == 0:
            cnt += 1
            visited[i][j] = 1
            num = grid[i][j]
            dfs(i, j)
        if cnt >= 4:
            ans += 1
        max_cnt = max(max_cnt, cnt)

print(ans, max_cnt)