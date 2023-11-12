x, y = map(int, input().split())

max_num = 0
for i in range(x, y+1):
    n_arr = list(map(int, list(str(i))))
    max_num = max(sum(n_arr), max_num)

print(max_num)