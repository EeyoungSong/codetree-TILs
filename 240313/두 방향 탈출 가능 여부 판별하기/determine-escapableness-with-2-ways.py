n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]

def in_range(r, c):
    return 0 <= r < n and 0 <= c < m

def dfs(r, c):
    for dr, dc in zip((1, 0), (0, 1)):
        nr, nc = r + dr, c + dc 
        if in_range(nr, nc) and grid[nr][nc] != 0 and visited[nr][nc] == 0:
            visited[nr][nc] = 1
            #print(nr, nc)
            dfs(nr, nc)


    
r, c = 0, 0
visited[r][c] = 1
dfs(r, c)
print(visited[n-1][m-1])