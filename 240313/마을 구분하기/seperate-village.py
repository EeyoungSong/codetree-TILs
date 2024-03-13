n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

def in_range(r, c):
    return 0 <= r < n and 0 <= c < n

def dfs(r, c):
    global cnt
    for dr, dc in zip((0, 1, 0, -1), (1, 0, -1, 0)):
        nr, nc = r + dr, c + dc
        if in_range(nr, nc) and grid[nr][nc] == 1 and not visited[nr][nc]:
            visited[nr][nc] = True
            #print(nr, nc)
            cnt += 1
            dfs(nr, nc)
    
    
num_arr = []
for r in range(n):
    for c in range(n):            
        if grid[r][c] == 1 and not visited[r][c]:
            visited[r][c] = True
            cnt = 1
            dfs(r, c)
            num_arr.append(cnt)
print(len(num_arr))
num_arr.sort()
for n in num_arr:
    print(n)

# r, c = 0, 0
# visted[r][c] = True
# print(dfs(r, c, 1))

# r, c = 4, 0
# visted[r][c] = True
# print(dfs(r, c, 1))