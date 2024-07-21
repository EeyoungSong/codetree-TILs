# n * n 격자
# k개의 시작점
# 상하좌우 인접한 곳으로만 이동 
# 이동 가능 (0) 이동 불가능 (1)
# 도달 가능한 칸의 수 구하기

from collections import deque
n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[0 for _ in range(n)] for _ in range(n)]

def in_range(r, c):
    return 0 <= r < n and 0 <= c < n

def can_go(r, c):
    return in_range(r, c) and not visited[r][c] and grid[r][c] == 0

def bfs():
    answer = 0
    while q:
        r, c = q.popleft()
        drs, dcs = [0, 1, 0, -1], [1, 0, -1, 0]
        for dr, dc in zip(drs, dcs):
            nr, nc = r + dr, c + dc
            if can_go(nr, nc):
                visited[nr][nc] = 1
                answer += 1
                q.append((nr, nc))

    return answer




q = deque()
answer = 0
for i in range(k):
    r, c = map(int, input().split())
    r, c = r - 1, c - 1
    if can_go(r, c):
        q.append((r, c))
        visited[r][c] = 1
        answer += 1
        answer += bfs()

print(answer)