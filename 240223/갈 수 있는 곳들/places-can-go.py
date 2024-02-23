# from collections import deque
# n, k = map(int, input().split())
# grid = [list(map(int, input().split())) for _ in range(n)]
# visited = [[0] * (n) for _ in range(n)]

# def in_range(r, c):
#     return 0 <= r < n and 0 <= c < n

# def bfs():
#     global cnt
#     while q:
#         r, c = q.popleft()
#         for dr, dc in ((1, 0), (0, 1), (-1, 0), (0, -1)):
#             nr, nc = r + dr, c + dc
#             if in_range(nr, nc) and grid[nr][nc] == 0 and not visited[nr][nc]:
#                 #print(nr, nc)
#                 visited[nr][nc] = 1
#                 cnt += 1
#                 q.append((nr, nc))

# q = deque()
# cnt = 0
# for i in range(k):
#     r, c = map(int, input().split())
#     r, c = r-1, c-1
#     if not visited[r][c]:
#         visited[r][c] = 1
#         cnt += 1
#         q.append((r, c))
#         bfs()

# print(cnt)

from collections import deque
n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * (n) for _ in range(n)]

def in_range(r, c):
    return 0 <= r < n and 0 <= c < n

def bfs():
    while q:
        global cnt
        r, c = q.popleft()
        for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            nr, nc = r + dr, c + dc
            if in_range(nr, nc) and grid[nr][nc] == 0 and not visited[nr][nc]:
                visited[nr][nc] = True
                cnt += 1
                q.append((nr, nc))

cnt = 0              
q = deque()
for i in range(k):
    r, c = map(int, input().split())
    r, c = r-1, c-1
    if grid[r][c] == 0 and not visited[r][c]:
        visited[r][c] = True
        cnt += 1
        q.append((r, c))
        bfs()



print(cnt)