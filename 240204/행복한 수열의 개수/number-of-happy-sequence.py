n, m = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]
ans = 0

garo_num_list = []
sero_num_list = []

for i in range(n):
    p = grid[i][0]
    cnt = 1
    for j in range(1, n):
        #print('p:', p)
        if p == grid[i][j]:
            cnt += 1
        else:
            cnt = 1
        p = grid[i][j]
    #print(cnt)
    if cnt >= m:
        ans += 1
        garo_num_list.append(i)   

for j in range(n):
    p = grid[0][j]
    cnt = 1
    for i in range(1, n):
        if p == grid[i][j]:
            cnt += 1
        else:
            cnt = 1
        p = grid[i][j]
        #print(p)
        
    if cnt >= m:
        ans += 1
        sero_num_list.append(j)

print(ans)
# print(garo_num_list)
# print(sero_num_list)