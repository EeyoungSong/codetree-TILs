from collections import deque
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]

# def bfs(): # n^2 시간복잡도
#      while q:
#         curr_v = q.popleft() #q에서 꺼낸 것 => current value
#         for next_v in graph[curr_v]: # 1~n까지 수 중
#             if not visited[next_v]: # 
#                 print(next_v)
#                 visited(next_v) = True
#                 q.append(next_v)

def in_range(r, c):
    return 0 <= r < n and 0 <= c < m

def bfs():
    while q:
        r, c = q.popleft()
        for dr, dc in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            nr, nc = r + dr, c + dc
            if in_range(nr, nc) and graph[nr][nc] == 1 and not visited[nr][nc]:
                #print(nr, nc)
                visited[nr][nc] = 1
                q.append((nr, nc))

q = deque()
visited[0][0] = 1
q.append((0, 0))

bfs()

print(visited[n - 1][m - 1])

# 연결 리스트가 연결된 모든 정점을 찾는 데(탐색)에는 이득.. 불필요한 탐색을 줄일 수 있음