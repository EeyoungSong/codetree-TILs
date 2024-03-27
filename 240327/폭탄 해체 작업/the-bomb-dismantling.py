n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

arr.sort(key=lambda x : (x[1], -x[0]))

score = 0
time = 1
for i in range(len(arr)):
    if arr[i][1] < time:
        continue
    time += 1
    score += arr[i][0]
    #print(time, score)

print(score)