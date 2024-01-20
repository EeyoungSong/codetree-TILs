n = int(input())
grid = [list(input()) for _ in range(n)]
k = int(input())
        
drs, dcs = [0, 1, 0, -1], [1, 0, -1, 0]
dir_num = ((k-1) // n + 1) % 4 


if dir_num == 1:
    r, c = 0, k-1
elif dir_num == 2:
    r, c = (k-1) % n, n-1
elif dir_num == 3:
    r, c = n-1, (n-1)- ((k-1) % n)
else:
    r, c = (k-1) % n, 0

#print(r, c)


def in_range(r, c):
    return 0 <= r < n and 0 <= c < n

def change_dir(slash, dir_num):
    if slash == "/":
        dir_num = 3 - dir_num
    else:
        if dir_num == 0 or dir_num ==2:
            dir_num += 1
        else:
            dir_num -= 1

    return dir_num

cnt = 1
while True:
    slash = grid[r][c]
    dir_num = change_dir(slash, dir_num)
    tr, tc = r + drs[dir_num], c + dcs[dir_num]
    if not in_range(tr, tc):
        break
    r, c = tr, tc
    cnt += 1

print(cnt)