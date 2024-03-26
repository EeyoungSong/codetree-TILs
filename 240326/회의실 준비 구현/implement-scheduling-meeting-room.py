MAX_NUM = 100000
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
arr.sort(key=lambda x : x[1])

used_arr = [0] * MAX_NUM


cnt = 0
m = 0
for i in range(0, len(arr)):
    if m > arr[i][0]:
        continue
    cnt += 1
    m = max(arr[i][1], m)
    #print(arr[i])
    for i in range(arr[i][0], arr[i][1]):
        used_arr[i] = 1

print(cnt)