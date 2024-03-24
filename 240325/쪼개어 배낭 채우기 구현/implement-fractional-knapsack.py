n, m = map(int, input().split())
arr = []
for _ in range(n):
    w, v = map(int, input().split())
    arr.append((w, v, v/w))

arr.sort(key=lambda x : x[2], reverse=True)

w_sum = 0
v_sum = 0
idx = 0
while True:
    if (m - w_sum) < arr[idx][0]:
        v_sum += arr[idx][1] * ((m - w_sum) / arr[idx][0])
        print("%.3f" % v_sum)
        break
    w_sum += arr[idx][0]
    v_sum += arr[idx][1]
    idx += 1
    if idx >= len(arr):
        print("%.3f" % v_sum)
        break