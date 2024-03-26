MAX_NUM = 100000
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
arr.sort(key=lambda x : x[1])

used_arr = [0] * MAX_NUM

cnt = 0
for elem in arr:
    if used_arr[elem[0]] != 0:
        continue
    cnt += 1
    for i in range(elem[0], elem[1]):
        used_arr[i] = 1

print(cnt)