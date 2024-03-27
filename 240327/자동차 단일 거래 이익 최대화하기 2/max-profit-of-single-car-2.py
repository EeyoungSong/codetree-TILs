n = int(input())
arr = list(map(int, input().split()))

# min_num = min(arr)
# idx = arr.index(min_num)
# max_num = max(arr[idx:])

# print(max_num - min_num)

max_num = max(arr)
idx = arr.index(max_num)
min_num = min(arr[:idx+1])

print(max_num - min_num)