offset = 100
MAX_NUM = 200
grid = [[0] * (MAX_NUM + 1) for _ in range(MAX_NUM + 1)]

n = int(input())

color = 'r'
for _ in range(n):
    a, b, c, d = map(int, input().split())
    for i in range(a, c):
        for j in range(b, d):
            #print(color)
            if color == 'r':
                grid[i+offset][j+offset] = 1
            else:
                grid[i+offset][j+offset] = 2
    if color == 'r':
        color = 'b'
    else:
        color = 'r'
            
            

ans = 0
for elem in grid:
    ans += elem.count(2)

print(ans)