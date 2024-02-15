n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*n for _ in range(n)]
ans = 0

def in_range(r, c):
    return 0 <= r < n and 0 <= c < n

def can_go(r, c):
    if in_range(r, c) and grid[r][c] != 0 and not visited[r][c]:
        return True
    return 

def dfs(r, c):
    global ans
    if r == n-1 and c == n-1:
        ans = 1
    
    drs, dcs = [0, 1], [1, 0]
    for dr, dc in zip(drs, dcs):
        nr, nc = r + dr, c + dc
        if can_go(nr, nc):
            visited[nr][nc] = True
            #print(nr, nc)
            dfs(nr, nc)




    # 갈 수 있는지 확인 
    # 오른쪽 아래쪽 dr, dc에 대해서 
    # visited = True 
    # dfs 호출 

dfs(0, 0)
print(ans)