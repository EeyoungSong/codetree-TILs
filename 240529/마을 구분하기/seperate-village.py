n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*n for _ in range(n)]

def in_range(r, c):
    return 0 <= r < n and 0 <= c < n

def dfs(r, c):
    global cnt

    drs, dcs = [0, 1, 0, -1], [1, 0, -1, 0]
    for dr, dc in zip(drs, dcs):
        nr, nc = r + dr, c + dc
        if not in_range(nr, nc) or grid[nr][nc] == 0 or visited[nr][nc] == 1:
            continue
        visited[nr][nc] = 1
        cnt += 1
        dfs(nr, nc)
    return

cnt_arr = []
for i in range(n):
    for j in range(n):
        if grid[i][j] == 1 and not visited[i][j]:
            cnt = 0
            dfs(i, j)
            cnt_arr.append(cnt)
print(len(cnt_arr))
for elem in sorted(cnt_arr):
    print(elem)