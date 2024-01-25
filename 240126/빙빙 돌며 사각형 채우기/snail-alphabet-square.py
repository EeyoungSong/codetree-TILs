n, m = map(int, input().split())

grid = [[0] * m for _ in range(n)]
alphabet_arr = [chr(i) for i in range(ord('A'), ord('Z')+1)]

drs, dcs = [0, 1, 0, -1], [1, 0, -1, 0]

def in_range(r, c):
    return  (0 <= r < n and 0 <= c < m) and grid[r][c] == 0

dir_num = 0

r, c = 0, 0
grid[0][0] = alphabet_arr[0]
cnt = 0
for i in range(1, n*m):
    tr, tc = r + drs[dir_num], c + dcs[dir_num] 
    if not in_range(tr, tc):
        dir_num = (dir_num + 1) % 4
        tr, tc = r + drs[dir_num], c + dcs[dir_num]
    cnt += 1
    r, c = tr, tc
    grid[r][c] = alphabet_arr[cnt % len(alphabet_arr)]
    # print(i, dir_num)

for i in range(n):
    for j in range(m):
        print(grid[i][j], end=" ")
    print()

# 종료조건을 어떻게 설정??