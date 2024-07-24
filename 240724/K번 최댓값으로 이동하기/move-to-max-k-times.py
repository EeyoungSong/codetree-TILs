# n * n 격자
# 1 ~ 100 숫자가 각 칸에 하나씩 주어져 있음
# 특정 위치에서 상하좌우만 이동
# 조건 1) 시작 위치에 적혀있는 숫자보다 작은 갈 수 있는 칸들 중
# 조건 2) 조건 1을 만족하는 숫자들 중 최댓값
# 조건 3) 조건 2를 만족하는 숫자가 여러개일 경우 행번호가 가장 작은 것 -> 열번호가 가장 작은 것
# -> 조건 1, 2, 3을 만족하는 r, c 찾아야함 - bfs로
# 이동을 k번 반복 & 더이상 이동 불가능하다면 종료
# k번 반복한 이후의 위치 (r, c)를 출력
from collections import deque

n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
# print(grid)


def in_range(r, c):
    return 0 <= r < n and 0 <= c < n

def can_go(r, c):
    return in_range(r, c) and not visited[r][c] and grid[r][c] < num
    


def bfs():
    max_idx = (n, n)
    max_num = 0
    while q:
        r, c = q.popleft()
        drs, dcs = [0, 1, 0, -1], [1, 0, -1, 0]
        for dr, dc in zip(drs, dcs):
            nr, nc = r + dr, c + dc
            
            if can_go(nr, nc):
                visited[nr][nc] = 1
                q.append((nr, nc))
                if grid[nr][nc] > max_num:
                    max_num = grid[nr][nc]
                    max_idx = (nr, nc)
                elif grid[nr][nc] == max_num and nr < max_idx[0]:
                    max_num = grid[nr][nc]
                    max_idx = (nr, nc)
                elif grid[nr][nc] >= max_num and nr == max_idx[0] and nc < max_idx[1]:
                    max_num = grid[nr][nc]
                    max_idx = (nr, nc)

     
    return max_idx



r, c = map(int, input().split())
r, c = r-1, c-1
q = deque()
visited = [[0] * n for _ in range(n)]
q.append((r, c))
num = grid[r][c]
r, c = bfs()
for i in range(1, k):
    q = deque()
    visited = [[0] * n for _ in range(n)]
    q.append((r, c))
    num = grid[r][c]
    r, c = bfs()


print(r+1, c+1)