n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]

r1, c1 = map(int, input().split())
r2, c2 = map(int, input().split())
r3, c3 = map(int, input().split())

def in_range(r, c):
    return 0 <= r < n and 0 <= c < n

def dfs(r, c):
    b = True
    drs, dcs = [0, 1, 0, -1], [1, 0, -1, 0]
    for dr, dc in zip(drs, dcs):
        nr, nc = r + dr, c + dc
        if in_range(nr, nc) and grid[nr][nc] == 1 and visited[nr][nc] == 0:
            for t in tuple_arr:
                if (nr, nc) == t:
                    b = False
            visited[nr][nc] = 1
            dfs(nr, nc)
    return b

arr = [(r1-1, c1-1), (r2-1, c2-1), (r3-1, c3-1)]          
tuple_arr = [(r2-1, c2-1), (r3-1, c3-1)]
for i, j in arr:
    if in_range(i, j) and grid[i][j] == 1 and visited[i][j] == 0:
        visited[i][j]
        print(i, j)
        print(dfs(i, j))
        tuple_arr.pop(0)