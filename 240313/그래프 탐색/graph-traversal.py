n, m = map(int, input().split())
arr = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)


def dfs(vertex):
    global cnt
    for elem in arr[vertex]:
        if not visited[elem]:
            cnt += 1
            visited[elem] = True
            #print(elem)
            dfs(elem)
            

cnt = 0
visited[1] = True
dfs(1)

print(cnt)