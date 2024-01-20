offset = 1000
MAX_NUM = 2000
grid = [[0] * MAX_NUM for _ in range(MAX_NUM)]


for _ in range(2):
    a, b, c, d = map(int, input().split())
    for i in range(a, c):
        for j in range(b, d):
            grid[i+offset][j+offset] = 1

a, b, c, d = map(int, input().split())
for i in range(a, c):
        for j in range(b, d):
            grid[i+offset][j+offset] += 2

ans = 0
for elem in grid:
    ans += elem.count(1)

print(ans)