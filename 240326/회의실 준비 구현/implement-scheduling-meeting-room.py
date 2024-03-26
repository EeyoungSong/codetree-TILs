MAX_NUM = 100000
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
arr.sort(key=lambda x : x[1])

used_arr = [0] * MAX_NUM

cnt = 0
for elem in arr:
    empty = True
    for i in range(elem[0], elem[1]):
        if used_arr[i] == 1:
            empty = False
    if empty == True:
        cnt += 1
        for i in range(elem[0], elem[1]):
            used_arr[i] = 1

print(cnt)