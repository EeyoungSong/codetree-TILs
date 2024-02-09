n, m, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
start = k-1

def is_empty(i, start):
    b = True
    for j in range(start, start+m):
        if grid[i][j] != 0:
            b = False
    return b

i = 0
while True:
    if i >= n or not is_empty(i, start):
        #print(i)
        for j in range(start, start+m):
            grid[i-1][j] = 1
        break
    i += 1

for arr in grid:
    for elem in arr:
        print(elem, end=" ")
    print()