n, t = map(int, input().split())
r, c, d = input().split()
r, c = int(r)-1, int(c)-1
dr, dc = [0, 1, 0, -1], [1, 0, -1, 0]
dir_dic = {'R' : 0, 'D' : 1, 'L': 2, 'U': 3}
dir_num = dir_dic[d]


def in_range(r, c):
    return 0 <= r < n and 0 <= c < n

time = 0
while True:
    if time >= t:
        break
    tr, tc = r + dr[dir_num], c + dc[dir_num]
    if in_range(tr, tc):
        r, c = tr, tc
    else:
        dir_num = (dir_num + 2) % 4
    time += 1
    # print(dir_num, r, c)

print(r+1, c+1)