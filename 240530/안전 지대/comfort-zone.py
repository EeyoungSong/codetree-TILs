import sys
sys.setrecursionlimit(3000)

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

def can_not_visit():
    for arr in visited:
        for elem in arr:
            if elem == 1:
                return False
    return True

def in_range(r, c):
    return 0 <= r < n and 0 <= c < m

def can_go(r, c):
    if in_range(r, c) and visited[r][c] == 0 and grid[r][c] > k:
        return True
    return


def dfs(r, c):
    drs, dcs = [0, 1, 0, -1], [1, 0, -1, 0]
    for dr, dc in zip(drs, dcs):
        nr, nc = r + dr, c + dc
        if can_go(nr, nc):
            visited[nr][nc] = 1
            # print(k, nr, nc, grid[nr][nc])
            dfs(nr, nc)


MAXNUM = 101
ans_arr = [0] * MAXNUM
br = False
for k in range(1, MAXNUM):
    if br:
        break
    cnt = 0
    visited = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if can_go(i, j):
                cnt += 1
                visited[i][j] = 1
                # print(k, i, j, grid[i][j])
                dfs(i, j)
    # print(cnt)
                
                
    ans_arr[k] = cnt
    if can_not_visit():
        br = True

ans = max(ans_arr)
if ans == 0:
    index = 1
else:
    index = ans_arr.index(ans)
print(index, ans)