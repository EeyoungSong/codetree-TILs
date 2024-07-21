# n, m 크기
# 상하좌우 인접한 칸으로만 이동
# 뱀이 있는 칸 이동 불가
# 구할 것 : 탈출 가능한 경로가 있는지

from collections import deque

n, m = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]
answer = [[0 for _ in range(m)]
            for _ in range(n)]

visited = [[0 for _ in range(m)]
            for _ in range(n)]

def in_range(r, c):
    return 0 <= r < n and 0 <= c < m

def can_go(r, c):
    return in_range(r, c) and not visited[r][c] and grid[r][c] == 1

def bfs():
    while q:
        r, c = q.popleft()
        drs, dcs = [0, 1, 0, -1], [1, 0, -1, 0]
        for dr, dc in zip(drs, dcs):
            nr, nc = r + dr, c + dc
            if can_go(nr, nc):
                visited[nr][nc] = 1
                answer[nr][nc] = 1
                q.append((nr, nc))

q = deque()
q.append((0, 0))
bfs()


print(answer[n-1][m-1])