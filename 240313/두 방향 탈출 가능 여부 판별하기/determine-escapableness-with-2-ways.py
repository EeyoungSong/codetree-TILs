n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(m)]
visited = [[0]*n for _ in range(m)]

def in_range(r, c):
    return 0 <= r < m and 0 <= c < n

def dfs(r, c):
    for dr, dc in zip((1, 0), (0, 1)):
        nr, nc = r + dr, c + dc 
        if in_range(nr, nc) and grid[nr][nc] != 0 and not visited[nr][nc]:
            visited[nr][nc] = 1
            #print(nr, nc)
            dfs(nr, nc)


    
r, c = 0, 0
visited[r][c] = 1
dfs(r, c)
print(visited[n-1][m-1])