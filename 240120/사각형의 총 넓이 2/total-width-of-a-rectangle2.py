offset = 100
MAX_NUM = 200
grid = [[0] * MAX_NUM for _ in range(MAX_NUM)]

n = int(input())

for _ in range(n):
    a, b, c, d = map(int, input().split())
    for i in range(a, c):
        for j in range(b, d):
            grid[i+offset][j+offset] = 1

ans = 0
for elem in grid:
    ans += elem.count(1)

print(ans)