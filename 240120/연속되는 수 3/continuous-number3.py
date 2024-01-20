n = int(input())

arr = [int(input()) for _ in range(n)]

max_num = 0
cnt = 1
for i in range(n):
    if i == 0 or (arr[i] < 0 and arr[i-1] > 0) or (arr[i] > 0 and arr[i-1] < 0):
        cnt = 1
    else:
        cnt += 1
    max_num = max(cnt, max_num)

print(max_num)