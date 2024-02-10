import copy
n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
set_arr = []
pos_arr = []
max_num = 0

def print_arr(grid):
    for arr in grid:
        print(arr)
    print()

def count(grid):
    cnt = 0
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                cnt += 1
    return cnt

def choose(max_num, set_arr, current_num):
    if current_num <= 0:
        #print(set_arr)
        temp = record(set_arr)
        #print_arr(temp)
        cnt = count(temp)
        max_num = max(max_num, cnt)
        return max_num

    for i in range(1, 4):
        set_arr.append(i)
        max_num = choose(max_num, set_arr, current_num-1)
        set_arr.pop()
    
    return max_num
    

def in_range(r, c):
    return 0 <= r < n and 0 <= c < n

def record(set_arr):
    temp = copy.deepcopy(grid)
    idx = 0
    for elem, b_num in zip(pos_arr, set_arr):
        r, c = elem

        if b_num == 1:
            for i in range(r-2, r+3):
                if in_range(i, c):
                    temp[i][c] = 1
    
        elif b_num == 2:
            drs, dcs = [0, 1, 0, -1], [1, 0, -1, 0]
            for i in range(4):
                nr, nc = r + drs[i], c + dcs[i]
                if in_range(nr, nc):
                    temp[nr][nc] = 1
        else:
            drs, dcs = [-1, -1, 1, 1], [-1, 1, -1, 1]
            for i in range(4):
                nr, nc = r + drs[i], c + dcs[i]
                if in_range(nr, nc):
                    temp[nr][nc] = 1
    return temp

for i in range(n):
    for j in range(n):
        if grid[i][j] == 1:
            pos_arr.append((i, j))

print(choose(max_num, set_arr, len(pos_arr)))