import copy

n = int(input())
arr = list(map(int, input().split()))

# min_num = min(arr)
# idx = arr.index(min_num)
# max_num = max(arr[idx:])

# print(max_num - min_num)

max_profit = 0
max_num = max(arr)
idx = arr.index(max_num)
min_num = min(arr[:idx+1])
arr = copy.deepcopy(arr[idx+1:])
max_profit = max(max_profit, max_num - min_num)

while len(arr) != 0:
    max_num = max(arr)
    idx = idx = arr.index(max_num)
    min_num = min(arr[:idx+1])
    arr = copy.deepcopy(arr[idx+1:])
    max_profit = max(max_profit, max_num - min_num)

print(max_profit)



# 뒤에서 반복하기