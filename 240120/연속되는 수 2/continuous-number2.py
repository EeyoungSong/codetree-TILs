n = int(input())

arr = [int(input()) for _ in range(n)]
max_num = 0
cnt = 1
for i in range(n):
    if i == 0 or arr[i] != arr[i-1]:
        cnt = 1
    else:
        cnt += 1
    if cnt >= max_num:
        max_num = cnt

        
print(max_num)