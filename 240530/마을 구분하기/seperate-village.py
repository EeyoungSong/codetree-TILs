n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
p_list = []


def in_range(r, c):
    return 0 <= r < n and 0 <= c < n

def can_go(r, c):
    if in_range(r, c) and grid[r][c] != 0 and not visited[r][c]:
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

ans_arr = []
for i in range(n):
    for j in range(n):
        if can_go(i, j):
            cnt = 1
            visited[i][j] = 1
            dfs(i, j)
            ans_arr.append(cnt)

print(len(ans_arr))
for elem in sorted(ans_arr):
    print(elem)